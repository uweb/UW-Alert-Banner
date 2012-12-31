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
 *  <script type="text/javascript" src="//washington.edu/static/alert.js"></script>
 *  </body>
 *  </html>
 *
 *  Full docs at:
 *  uw.edu/marketing/uw-alert-banner/
 *
 *--------------------------------------------------------------------------*/

// Thanks Dane!
var strTestStatus = window.location.hash.indexOf('uwalert') === -1 ? 'false' : 'true';
// Allow for local testing
var strDomain = (window.location.hostname == 'localhost') ? 'localhost' : 'www.washington.edu/static';
var strDataFeed = '/UW-Alert-Banner/alert/?c=displayAlert&test='+strTestStatus;
var strBaseUrl = window.location.protocol + '//' + strDomain;

var strScript = document.createElement('script');
strScript.setAttribute('src', strBaseUrl + strDataFeed);
document.getElementsByTagName('head')[0].appendChild(strScript); 

// displayAlert - grab content to display message 
function displayAlert(objAlertData)
{

    // Just in case w.com delivers us something bad
    // or We don't care if the feed is null
    if ((!objAlertData) || (objAlertData.found == 0))
        return false;

    // Alert colors
    arrAlertTypes = {
        'red-alert-urgent' : 'uwalert-red',
        'orange-alert'     : 'uwalert-orange',
        'steel-alert-fyis' : 'uwalert-steel'
    };

    var arrCategories = objAlertData.posts[0].categories;
    // If there is a test alert 
    if ( window.location.hash.indexOf('uwalert') != -1 )
    {
        // Sometimes we don't get a category from the w.com test feed
        var objFakeCat = new Object();
        var strTestAlertColor = window.location.hash.replace('#','');
        objFakeCat.slug = strTestAlertColor;
        arrCategories['Fake Category'] = objFakeCat;
    }

    var strSuccess = false;
    for (strCategory in arrCategories)
    {
        var objCategory = arrCategories[strCategory];
        // Quick way to determine color
        if (arrAlertTypes[objCategory.slug] || objFakeCat)
        {
            var strAlertTitle    = objAlertData.posts[0].title;
            var strAlertLink     = 'http://emergency.washington.edu/';
            var strAlertMessage  = objAlertData.posts[0].excerpt;
            var strAlertColor    = arrAlertTypes[objCategory.slug] ? arrAlertTypes[objCategory.slug] : objFakeCat.slug;
            strSuccess           = true;
        }
    }

    // Banners must have an actual color
    // Don't load anything unless we have something to present
    if (strSuccess) 
    {
        addElement(strAlertTitle,strAlertLink,strAlertColor,strAlertMessage);
        // Code contributed by Dustin Brewer
        var strCSS = document.createElement('link');
        strCSS.setAttribute('href', strBaseUrl + '/UW-Alert-Banner/uwalert.css');
        strCSS.setAttribute('rel','stylesheet');
        strCSS.setAttribute('type','text/css');
        document.getElementsByTagName('head')[0].appendChild(strCSS);
        // Because content is loaded dynamically, need to wait to grab the height
        setTimeout(function() {
            var strHeight = document.getElementById('uwalert-alert-message').offsetHeight;
            var bodyTag = document.getElementsByTagName('body')[0];
            bodyTag.style.backgroundPosition='0px '+strHeight+'px';
        },10);

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
    bodyTag.className += ' uw-alert';

    var wrapperDiv = document.createElement('div');
    wrapperDiv.setAttribute('id','uwalert-alert-message');
    wrapperDiv.setAttribute('class', strAlertColor);

    var alertBoxTextDiv = document.createElement('div');
    alertBoxTextDiv.setAttribute('id','uwalert-alert-inner');
    alertBoxTextDiv.setAttribute('class', strAlertColor);

    var anchorLink = document.createElement('a');
    anchorLink.setAttribute('href', strAlertLink);
    anchorLink.setAttribute('title', strAlertTitle);

    var header1 = document.createElement('div');
    header1.setAttribute('id', 'uwalert-alert-header');

    // Supporting titles with special characters
    try 
    {
        anchorLink.innerHTML = strAlertTitle;
    }
    catch (err)
    {
        var header1Text = document.createTextNode(strAlertTitle);
        anchorLink.appendChild(header1Text);

    }
    header1.appendChild(anchorLink);
    
    var alertTextP = document.createElement('p');

    var div = document.createElement("div");
    div.innerHTML = strAlertMessage;
    // Strip out html that wordpress.com gives us
    var alertTextMessage = div.textContent || div.innerText || "";
    // Build alert text node and cut of max characters
    var alertText = document.createTextNode(
    alertTextMessage.substring(0,360) + 
        (alertTextMessage.length >= 360 ? '... ' : ' ')
    );
    alertTextP.appendChild(alertText);

    var alertLink = document.createElement('a');
    alertLink.setAttribute('href', strAlertLink);
    alertLink.setAttribute('title', strAlertTitle);
    var alertLinkText = document.createTextNode('More Info');
    alertLink.appendChild(alertLinkText);

    // Start Building the Actual Div
    alertTextP.appendChild(alertLink);

    alertBoxTextDiv.appendChild(header1);
    alertBoxTextDiv.appendChild(alertTextP);

    wrapperDiv.appendChild(alertBoxTextDiv);

    bodyTag.insertBefore(wrapperDiv, bodyTag.firstChild);
} 
