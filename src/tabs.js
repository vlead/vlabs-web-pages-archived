function newTabs () {
	var links = document.getElementsByClassName('lab-list-row-div')
	for ( i = 0 ; i < links.length ; i ++ ) {
		labLink = links[i].firstChild.nextSibling.firstChild.nextSibling
		labLink.setAttribute('target', '_blank')
		labLogo = links[i].firstChild.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling	
		labLogo.setAttribute('target', '_blank')
		lectureLogo = labLogo.nextSibling.nextSibling.firstChild.nextSibling
		lectureLogo.setAttribute('target', '_blank')
	}
}

window.onload = function(){ newTabs() }