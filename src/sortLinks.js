window.onload = function () { sortLinks() }
sortLinks = function () {
	links = document.getElementsByClassName('sidebar-a')
	for ( i = 9 ; i <= links.length - 1 ; i ++ ) {
		alert(links[i].innerHTML)
	}
}