function prefilled()
{
	var url = window.location.href, FormName = "myForm";
	if(url.indexOf('?') > -1)
		return;
	else
	{
		var list = url.split('?');
		for(var i = 0 ; i < list.length ; i++)
		{
			var list1 = list[i].split('=')
			eval(document+ '.' + FormName + '.' + list1[0] + '.value ="' + list1[1] + '"');
		}
	}
}