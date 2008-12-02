/*  University of Washington - Alert 1.0 Beta
 *  (c) 2008 Chris Heiland, Tim Chang-Miller
 *
 *  Script should be included like such:
 *  
 *  <html>
 *  <head>
 *  <title>Page Title</title>
 *  <script type="text/javascript" src="http://depts.washington.edu/uweb/scripts/alert.js"></script>
 *  </head>
 *  <body>
 *  
 *  <script type="text/javascript">
 *  	getMessage();
 *  </script>
 *  </body>
 *  </html>
 *
 *--------------------------------------------------------------------------*/

/*
 * Include our javascript object script, the wonderful Prototype... and friends
 *---------------------------*/

document.domain = 'washington.edu';
 
 // getCookie - Stolen from the tubes, grab cookie by name
function getCookie(cookieName)
{
    var arrResults = document.cookie.match ( '(^|;) ?' + cookieName + '=([^;]*)(;|$)' );

    if ( arrResults )
        return ( unescape ( arrResults[2] ) );
    else
        return null;
}

// The problem is XMLHttpRequest is an AJAX call, which means cross domain
// even subdomains will fail, need to find another method
function AJ()
{
	var obj;
	if (window.XMLHttpRequest)
        obj = new XMLHttpRequest();
	else if (window.ActiveXObject)
    {
		try
        {
			obj = new ActiveXObject('MSXML2.XMLHTTP.3.0');
		}
		catch(er)
        {
			try
            {
				obj = new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch(er)
            {
				obj = false;
			}
		}
	}
	return obj;
}

function isThere(strURL)
{
	var req = new AJ(); // XMLHttpRequest object
	try
    {
        // This line does not work - bah
		req.open('HEAD', strURL, false);
        req.send(null);
		return req.status == 200 ? true : false;
	}
	catch (er)
    {
		return false;
	}
}

// var strStatusMess = isThere('http://depts.washington.edu/uweb/emergency/emergency');
// alert(strStatusMess);

// Don't output the stylesheet if the alert box was closed
// If we do the crontob for get_rss then we have to go this route, otherwise we can 
//getCookie('uwalertcolor') // This would work if the get_rss is set by crontab
//isThere('http://depts.washington.edu/uweb/emergency/emergency') // This would work on crontab
// So why are we doing the isThere?

// Some Condition?!?

if (isThere('emergency-uweb-28462'))
{
    // Dynamically set the next either from category or another method
    // Need to find another way - Cookie is bad - For now 
    var strAlertColor = 'red' //getCookie('uwalertcolor');
    // PHP Function/Script that returns the color?

    // If the file does not exist - then don't show
    
    // Might have to do some additional work here
    // Probably less effecient but much easier to read
    // -------
    // What do we do for the 98% of the time when the cookie is not set and there is no RSS items?
    document.write('<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/prototype.js"><\/script>' +
    '<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/scriptaculous.js?load=effects"><\/script>' +
    '<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/emergency.js"><\/script>');
    //var strAlertMessage = isThere('http://depts.washington.edu/uweb/');
    //alert(strAlertMessage);
    
    var strStyle = strAlertColor == 'red' ? 'uwalert_red.css' : 'uwalert_orange.css';
    document.write('<link href="http://depts.washington.edu/uweb/emergency/'+ strStyle +'" rel="stylesheet" type="text\/css" \/>' +
    '<sty' + 'le type="text\/css"><!-- body { margin: 0; padding: 0; } --><\/style>');
}
else
{
    function displayAlert()
    {
        // Does nothing - for error prevention
    }   
}