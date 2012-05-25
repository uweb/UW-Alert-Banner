$(document).ready(function() {

  $.getJSON('alert.json', function(data) {

    // Alert colors  TODO Test alert slug
    types = {
        'red-alert'     : 'red',
        'orange-alert'  : 'orange',
        'blue-alert'    : 'blue',
        'steel-alert'   : 'steel',
        'campus-info'   : 'red',
    };
 
    $.each(data.posts[0].categories, function(key,val) {
      if (types[val.slug]) {
        // Fire up alert
        var strAlertTitle = data.posts[0].title;
        var strAlertLink = 'http://emergency.washington.edu/';
        var strAlertMessage = data.posts[0].excerpt;
        var strAlertColor = types[val.slug];

        addElement(strAlertTitle,strAlertLink,strAlertMessage,strAlertColor);
      }
    });

  });

});

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

var strCSS = document.createElement('link');
strCSS.setAttribute('href', '//www.washington.edu/static/uwalert.css');
strCSS.setAttribute('rel','stylesheet');
strCSS.setAttribute('type','text/css');
$(strCSS).appendTo('head');

// addElement - display HTML on page right below the body page
// don't want the alert to show up randomly
function addElement(strAlertTitle,strAlertLink,strAlertMessage,strAlertColor)
{
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
  // FIXME not correctly displaying as encoded html
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

  // Grab the tag to start the party
  var bodyTag = document.getElementsByTagName('body')[0];

  bodyTag.style.margin = '0px';
  bodyTag.style.padding = '0px';

  bodyTag.insertBefore(wrapperDiv, bodyTag.firstChild);
}
