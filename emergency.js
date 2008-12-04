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

// Object Creation for message to carry through functions
var oMessage = getMessage();

// getMessage - grab HTML from get_message.php
function getMessage()
{
    // Full URL won't want to work - Cross Domain and all that - proxy server
    //  Figure out prior to offering service
    var strGetMsgUrl = 'get_rss.php';

    var strDecayRate = 3;

    return new Ajax.PeriodicalUpdater('alertMessage', strGetMsgUrl, {
   	    method: 'post', // using POST to combat IE caching,
   	    decay: strDecayRate, // Resets if there is a change in the response
        frequency: 60000 // Going on vaca - don't pull much
   	});
}

// displayAlert - wrapper to display message 
function displayAlert()
{
    addElement();
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
function hideit(id)
{    
    oMessage.stop();
}
