
function lw(d,typ,sub,name,opt) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET","http://192.168.29.218/cgi-bin/docker.py?y=" + typ + "&z=" + sub + "&o=" + opt + "&n=" + name, true);
	xhr.send();
	xhr.onload = function () {
		var output = xhr.responseText;
		document.getElementById(d).innerHTML = output;
	}
}
