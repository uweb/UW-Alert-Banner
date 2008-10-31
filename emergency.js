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

// Object Creation for message to carry through functions
var oMessage = getMessage();

// getMessage - grab HTML from get_message.php
function getMessage()
{
    var strGetMsgUrl = 'get_message.php';
    
    return new Ajax.PeriodicalUpdater('alertMessage', strGetMsgUrl, {
	    method: 'post', // using POST to combat IE caching,
	    frequency: 10
	});
}

// displayAlert - check for cookie before  displaying message
// don't display if they have closed the alert
function displayAlert()
{
    if ( getCookie('uwalerthide') )
    {
        oMessage.stop();
    }
    else
    {
        addElement();
    }
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

// hideit - external function tied to close button
// sets the cookie and closes the alert
function hideit(id)
{
    $('alertBox').hide();
    
    var cookieDate = new Date();
    var strExpDate = cookieDate.getTime();
    strExpDate += 3600*1000; //expires in 1 hour (milliseconds) 
    cookieDate.setTime(strExpDate);
    
    document.cookie = 'uwalerthide=yes;expires=' +
        cookieDate.toGMTString();

    oMessage.stop();
}