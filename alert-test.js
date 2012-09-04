/*  University of Washington - Alert 2.0 Beta
 *  (c) 2011 Chris Heiland
 *
 *  Script should be included like such:
 * 
 *  <html>
 *  <head>
 *  <title>Page Title</title>
 *  </head>
 *  <body>
 * 
 *  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
 *  <script type="text/javascript" src="//washington.edu/static/alert.js"></script>
 *  </body>
 *  </html>
 *
 *  Full docs at:
 *  uw.edu/externalaffairs/uwmarketing/toolkits/uw-alert-banner/
 *
 *--------------------------------------------------------------------------*/

var strProto = (window.location.protocol == 'https:') ? 'https://' : 'http://';

// Code contributed by Dustin Brewer
var strCSS = document.createElement('link');
strCSS.setAttribute('href', strProto + 'www.washington.edu/static/uwalert.css');
strCSS.setAttribute('rel','stylesheet');
strCSS.setAttribute('type','text/css');
document.getElementsByTagName('head')[0].appendChild(strCSS);

// displayAlert - grab content to display message 
function displayAlert()
{
    // Alert colors
    types = {
      'red-alert-urgent' : 'uw-alertred',
      'orange-alert'     : 'uw-alertorange',
      'steel-alert-fyis' : 'uw-alertsteel'
    };
    
    var strAlertTitle = 'Campus\ Alert\:';
    var strAlertLink = 'http://emergency.washington.edu/';
    var strAlertMessage = 'There\ is\ no\ emergency\.\ \ For\ additional\ information\,\ please\ visit\ ';
    var strAlertColor = 'steel';
        
    // Banners must have an actual color
    if (strAlertColor)
    {
        addElement(strAlertTitle,strAlertLink,strAlertColor,strAlertMessage);
    }
}

// addElement - display HTML on page right below the body page
// don't want the alert to show up randomly
function addElement(strAlertTitle,strAlertLink,strAlertColor,strAlertMessage)
{
  // Grab the tag to start the party
  var bodyTag = document.getElementsByTagName('body')[0];
  
  bodyTag.style.margin = '0px';
  bodyTag.style.padding = '0px';

  var wrapperDiv = document.createElement('div');
  wrapperDiv.setAttribute('id','uwalert-alertMessage');

  var alertBoxDiv = document.createElement('div');
  alertBoxDiv.setAttribute('id', 'uwalert-alertBox');
  alertBoxDiv.setAttribute('class', strAlertColor);

  var alertBoxTextDiv = document.createElement('div');
  alertBoxTextDiv.setAttribute('id', 'uwalert-alertBoxText');
  
  var header1 = document.createElement('h1');
  var header1Text = document.createTextNode('Campus Alert:');
  header1.appendChild(header1Text);

  var alertTextP = document.createElement('p');

  // Wordpres includes html, this won't do
  // var alertText = document.createTextNode(strAlertMessage);
  // alertTextP.appendChild(alertText);

  var div = document.createElement("div");
  div.innerHTML = strAlertMessage;
  // Strip out html that wordpress.com gives us
  var alertTextMessage = div.textContent || div.innerText || "";
  // Build alert text node and cut of max characters
  var alertText = document.createTextNode(
    alertTextMessage.substring(0,200) + 
    (alertTextMessage.length >= 200 ? '... ' : ' ')
  );
  alertTextP.appendChild(alertText);


  var alertLink = document.createElement('a');
  alertLink.setAttribute('href', strAlertLink);
  alertLink.setAttribute('title', strAlertTitle);
  var alertLinkText = document.createTextNode('More Info');
  alertLink.appendChild(alertLinkText);

  var gtText = document.createTextNode(' >>');
  
  var clearDiv = document.createElement('div');
  clearDiv.setAttribute('id', 'uwalert-clearer');

  // Start Building the Actual Div
  alertTextP.appendChild(alertLink);
  alertTextP.appendChild(gtText);

  alertBoxTextDiv.appendChild(header1);
  alertBoxTextDiv.appendChild(alertTextP);

  alertBoxDiv.appendChild(alertBoxTextDiv);
  alertBoxDiv.appendChild(clearDiv);

  wrapperDiv.appendChild(alertBoxDiv);
  
  bodyTag.insertBefore(wrapperDiv, bodyTag.firstChild);
} 

displayAlert();
