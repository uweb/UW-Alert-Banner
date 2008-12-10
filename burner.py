#!/usr/local/bin/python2.5

"""
Summary: script to run in cronjob - detect if there is something to post
if so, then output content to the alert.js file and include everything 
needed.  If no alert, then just output skeleton file.
"""

import os, urllib2, re
import uwlibweb, feedparser
#import librss  

strHeader = """
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
""";
# Constants
RED = 4;
ORANGE = 6;

# This slows the script down dramatically as it has to go out to the world and check the resource

strAlertRed = feedparser.parse(uwlibweb.getFeedData(RED))
strAlertOrange = feedparser.parse(uwlibweb.getFeedData(ORANGE))

try:
    strAlertStatus = uwlibweb.getHighest(strAlertRed.entries[0].date_parsed, strAlertOrange.entries[0].date_parsed)
except:
    strAlertStatus = 0

if strAlertStatus:
    # Do something interesting here
    intCategory = ''
    strAlertColor = ''
    
    # Ignoring if both dates ar the same
    if strAlertStatus == 1:
        strAlert = strAlertRed;
        strAlertColor = 'red';
        intCategory = RED;
    elif strAlertStatus == 2:
        strAlert = strAlertOrange;
        strAlertColor = 'orange';
        intCategory = ORANGE;

    #Save the rss data
    #uwlibweb.saveData('emergency.rss', strAlert)
        
    # Take newest item and display
    strTitle = strAlert.entries[0].title
    strLink = 'http://emergency.washington.edu/'
    strDesc = strAlert.entries[0].description
    strDate = strAlert.entries[0].date
    
    strContent = strDesc[:180] + '... '

    if strDesc and strTitle:
        strContent += '<a href="' + strLink + '" title ="' + strTitle + '">More Info</a> &gt;&gt;'

    strHTMLContent = """
<div id="alertBox">
<div id="alertBoxText">
        <h1>Campus Alert:</h1>
        <p>%s <span>(%s)</span></p>
    </div>
    <div id="clearer"></div>
</div> """ % (strContent, strDate)

    # Set alert color based on file contents
    if strAlertColor == 'red':
        strStyle = 'uwalert_red.css'
    elif strAlertColor == 'orange':
        strStyle = 'uwalert_orange.css'

    strContent = """
document.write('<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/prototype.js"><\/script>' +
'<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/scriptaculous.js?load=effects"><\/script>');

document.write('<link href="http://depts.washington.edu/uweb/emergency/%s" rel="stylesheet" type="text\/css" \/>' +
    '<sty' + 'le type="text\/css"><!-- body { margin: 0; padding: 0; } --><\/style>');

// displayAlert - grab HTML to display message 
function displayAlert()
{
    // How best to insert HTML?
    var strAlertMessageHTML = '%s';
    // Can we pass to the following function?
    addElement(strAlertMessageHTML);
}

// addElement - display HTML on page right below the body page
// don't want the alert to show up anywhere
function addElement(strAlertMessageHTML)
{
  var bodyTag = document.getElementsByTagName('body')[0];

  var newDiv = document.createElement('div');
  var divIdName = 'alertMessage';
  
  newDiv.setAttribute('id',divIdName);
  newDiv.innerHTML = strAlertMessageHTML;

  bodyTag.insertBefore(newDiv, bodyTag.firstChild);
}
""" % (strStyle, re.escape(strHTMLContent))
else:
    strContent = """
function displayAlert()
{
    // This is where some code should go so people
    // Can test the warning system in some way
    // Optional parameters come to mind
    // Does nothing - for error & warning prevention
}
    """

strOutput = strHeader + strContent + "\n";

try:
    strFileout = '/rc22/d10/uweb/public_html/emergency/alert.js'
    objFile = open(strFileout, "w")
    objFile.write(strOutput)
    objFile.close()
except Exception, strError:
    print "Error Writing to File %s because %s" % (strFilename, strError)