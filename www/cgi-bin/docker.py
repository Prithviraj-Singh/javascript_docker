#!/usr/bin/python3

print("content-type: text/html","\n")

import cgi
import subprocess

obj = cgi.FieldStorage()
docker = "docker "
typ = obj.getvalue("y")
sub = obj.getvalue("z")
opt = obj.getvalue("o")
name = obj.getvalue("n")
space = " "
print("Output:")
if typ == None:
    typ = ""

if sub == None:
    sub = ""

if opt == None:
    opt = ""
if name == None:
    name = ""
print(docker+space+typ+space+sub+space+opt+space+name)
o = subprocess.getoutput(docker+space+typ+space+sub+space+opt+space+name)
print("<pre/>",o)
