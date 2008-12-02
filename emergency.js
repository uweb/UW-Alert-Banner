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
 *  	displayAlert();
 *  </script>
 *  </body>
 *  </html>
 *
 *--------------------------------------------------------------------------*/

document.domain = 'washington.edu';
 
// Object Creation for message to carry through functions
//var oMessage = getMessage();

// getMessage - grab HTML from get_message.php
function getMessage()
{
    // Full URL that doesn't seem to want to work right
    //'http://depts.washington.edu/uweb/emergency/get_message.php'
    var strGetMsgUrl = 'emergency-uweb-28462/get_message.php';
    var strAvailable = isThere(strGetMsgUrl);
    // This does not seem to work as designed
    //var strDecayRate = 0;
    //strDecayRate = isThere('http://staff.washington.edu/cheiland/alert/emergency') ? 1 : 10;
    if (strAvailable)
    {
//        return new Ajax.PeriodicalUpdater('alertMessage', strGetMsgUrl, {
//    	    method: 'post', // using POST to combat IE caching,
//    	    frequency: 3
            //decay: strDecayRate // Resets if there is a change in the response
//    	});
    }
    else
    {
        throw "Error: Can't Access Alert Message"; 
    }
}

// displayAlert - check for cookie before  displaying message 
// don't display if they have closed the alert
function displayAlert()
{
    // if ( getCookie('uwalerthide') )
    // {
        // oMessage.stop();
    // }
    // else
    // {
        addElement();
    // }
}

// addElement - display HTML on page right below the body page
// don't want the alert to show up anywhere
function addElement() 
{
  var bodyTag = document.getElementsByTagName('body')[0];

  var newDiv = document.createElement('div');
  var divIdName = 'alertMessage';
  
  newDiv.setAttribute('id',divIdName);

  bodyTag.insertBefore(newDiv, bodyTag.firstChild);
}

// setCookie - Another function stolen from the tubes
//http://techpatterns.com/downloads/javascript_cookies.php
function setCookie( strName, strValue, strExpires, strPath, strDomain, strSecure ) 
{
    // set time, it's in milliseconds
    var strToday = new Date();
    strToday.setTime( strToday.getTime() );

    strPath = '/';
    strDomain = '.washington.edu';
    
     /*
            if the strExpires variable is set, make the correct 
            strExpires time, the current script below will set 
            it for x number of days, to make it for hours, 
            delete * 24, for minutes, delete * 60 * 24
            */
    if ( strExpires )
    {
        // Original was set for days, we want to set it for hours
        //strExpires = strExpires * 1000 * 60 * 60 * 24;
        strExpires = strExpires * 1000 * 60 * 60;
    }
    var expiresDate = new Date( strToday.getTime() + (strExpires) );

    document.cookie = strName + "=" + escape( strValue ) +
    ( ( strExpires ) ? ";expires=" + expiresDate.toGMTString() : "" ) + 
    ( ( strPath ) ? ";path=" + strPath : "" ) + 
    ( ( strDomain ) ? ";domain=" + strDomain : "" ) +
    ( ( strSecure ) ? ";secure" : "" );
}


// hideit - external function tied to close button
// sets the cookie and closes the alert
function hideit(id)
{    
    setCookie('uwalerthide' , 'yes' , 1);
        
    oMessage.stop();
}
