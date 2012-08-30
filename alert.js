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

var strScript = document.createElement('script');
// script.setAttribute('src', '//www.washington.edu/static/alert-test.json');
strScript.setAttribute('src', strProto + 'public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish&callback=displayAlert');
document.getElementsByTagName('head')[0].appendChild(strScript); 

// Code contributed by Dustin Brewer
var strCSS = document.createElement('link');
strCSS.setAttribute('href', strProto + 'www.washington.edu/static/uwalert.css');
strCSS.setAttribute('rel','stylesheet');
strCSS.setAttribute('type','text/css');
document.getElementsByTagName('head')[0].appendChild(strCSS);

// displayAlert - grab content to display message 
function displayAlert(data)
{
    // We don't care if there's nothing
    if (data.found == 0) {
        return false;
    }

    // Alert colors
    types = {
      'red-alert-urgent' : 'red',
      'orange-alert'     : 'orange',
      'steel-alert-fyis' : 'steel',
      'test'             : 'steel'
    };
    
    for (strCategory in data.posts[0].categories ) {
        var objCategory = data.posts[0].categories[strCategory]
        // console.log(objCategory);
        if (types[objCategory.slug]) {
            var strAlertTitle  = data.posts[0].title;
            var strAlertLink   = 'http://emergency.washington.edu/';
            var strAlertMessage = data.posts[0].excerpt;
            var strAlertColor = types[objCategory.slug];
        }
        
    }
    
    addElement(strAlertTitle,strAlertLink,strAlertColor,strAlertMessage);
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
  wrapperDiv.setAttribute('id','alertMessage');

  var alertBoxDiv = document.createElement('div');
  alertBoxDiv.setAttribute('id', 'alertBox');
  alertBoxDiv.setAttribute('class', strAlertColor);

  var alertBoxTextDiv = document.createElement('div');
  alertBoxTextDiv.setAttribute('id', 'alertBoxText');
  
  var header1 = document.createElement('h1');
  var header1Text = document.createTextNode('Campus Alert:');
  header1.appendChild(header1Text);

  var alertTextP = document.createElement('p');

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

// displayAlert();
