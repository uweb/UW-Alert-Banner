/*  University of Washington - Alert 2.0 Beta
 *  (c) 2011 Chris Heiland, Tim Chang-Miller
 *
 *  Script should be included like such:
 * 
 *  <html>
 *  <head>
 *  <title>Page Title</title>
 *  <script type="text/javascript" src="http://emergency.washington.edu/alert.js"></script>
 *  </head>
 *  <body>
 * 
 *  <script type="text/javascript">
 *    displayAlert();
 *  </script>
 *  </body>
 *  </html>
 *
 *  Full docs at:
 *  uw.edu/externalaffairs/uwmarketing/toolkits/uw-alert-banner/
 *
 *--------------------------------------------------------------------------*/
// Code contributed by Dustin Brewer
var strProto = (window.location.protocol == 'https:') ? 'https://' : 'http://';
var strCSS = document.createElement('link');
strCSS.setAttribute('href', strProto + 'emergency.washington.edu/uwalert_red.css');
strCSS.setAttribute('rel','stylesheet');
strCSS.setAttribute('type','text/css');
document.getElementsByTagName('head')[0].appendChild(strCSS);
// addElement - display HTML on page right below the body page
// don't want the alert to show up randomly
function addElement(strAlertTitle,strAlertLink,strAlertMessage)
{
  // Grab the tag to start the party
  var bodyTag = document.getElementsByTagName('body')[0];

  bodyTag.style.margin = '0px';
  bodyTag.style.padding = '0px';

  var wrapperDiv = document.createElement('div');
  wrapperDiv.setAttribute('id','alertMessage');

  var alertBoxDiv = document.createElement('div');
  alertBoxDiv.setAttribute('id', 'alertBox');

  var alertBoxTextDiv = document.createElement('div');
  alertBoxTextDiv.setAttribute('id', 'alertBoxText');

  var header1 = document.createElement('h1');
  var header1Text = document.createTextNode('Campus Alert:');
  header1.appendChild(header1Text);

  var alertTextP = document.createElement('p');
  var alertText = document.createTextNode(strAlertMessage);
  alertTextP.appendChild(alertText);

  var alertLink = document.createElement('a');
  alertLink.setAttribute('href', strAlertLink);
  alertLink.setAttribute('title', strAlertTitle);
  var alertLinkText = document.createTextNode('More Info');
  alertLink.appendChild(alertLinkText);

  var gtText = document.createTextNode(' >>');

  var clearDiv = document.createElement('div');
  clearDiv.setAttribute('id', 'clearer');

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

// displayAlert - grab content to display message 
function displayAlert()
{
    var strAlertTitle = 'Incoming\ Asteroid';
    var strAlertLink = 'http://emergency.washington.edu/';
    var strAlertMessage = 'DESC\:\ Astroid\ Fatal';

    addElement(strAlertTitle,strAlertLink,strAlertMessage);
}
