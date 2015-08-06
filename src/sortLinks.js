window.onload = function () { sortLinks() }
sortLinks = function () {
	sortedLinks = []
	parent = []
	links = document.getElementsByClassName('sidebar-a')
	for ( i = 9 ; i <= links.length - 1 ; i ++ ) {
		sortedLinks.push(links[i])
	}
	
	for ( i = 0 ; i < sortedLinks.length ; i ++ ) {
		sortedLinks[i].innerHTML = sortedLinks[i].innerHTML.trim()
	}
	sortedLinks.sort()
	for ( i = 0 ; i < sortedLinks.length ; i ++ ) {
		parent.push(sortedLinks[i].parentNode.parentNode.parentNode)
	}
}