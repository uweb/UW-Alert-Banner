#!/usr/local/bin/python2.5

"""
Summary: script to run in cronjob - detect if there is something to post
if so, then output content to the alert.js file and include everything 
needed.  If no alert, then just output skeleton file.
"""

import os, re
import uwlibweb, feedparser
from datetime import timedelta, datetime

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
"""
## 4 & 6 are test categories
## Alert Status (WP Categories)
## 7 Publish
## 8 - Red Alert 
## 9 - Orange Alert    
## Well you get the idea
# Constants / (WordPress Categories)
RED = 8
ORANGE = 9
BLUE = 10
STEEL = 12

strHTMLContent = """
<div id="alertBox">
<div id="alertBoxText">
        <h1>Campus Alert:</h1>
        <p>There is no emergency.  For additional information, 
        please visit <a href="http://emergency.washington.edu">emergency.washington.edu</a></p>
    </div>
    <div id="clearer"></div>
</div> """

# We want to make sure there are no problems with a lock of a post
# If there are any problems, just set the date to zero
hashAlertDate = {} # What is the game from using a hash instead of strings?
try:
    strAlertRed = feedparser.parse(uwlibweb.getFeedData(RED))
    hashAlertDate['red'] = convertEpoch(strAlertRed.entries[0].date_parsed)
except:
    hashAlertDate['red'] = 0

try:
    strAlertOrange = feedparser.parse(uwlibweb.getFeedData(ORANGE))
    hashAlertDate['orange'] = convertEpoch(strAlertOrange.entries[0].date_parsed)
except:
    hashAlertDate['orange'] = 0

try:
    strAlertBlue = feedparser.parse(uwlibweb.getFeedData(BLUE))
    hashAlertDate['blue'] = convertEpoch(strAlertBlue.entries[0].date_parsed)
except:
    hashAlertDate['blue'] = 0

try:
    strAlertSteel = feedparser.parse(uwlibweb.getFeedData(STEEL))
    hashAlertDate['steel'] = convertEpoch(strAlertSteel.entries[0].date_parsed)
except:
    hashAlertDate['steel'] = 0
    
# No alert is a good Alert
strAlertStatus = 0

# Need an array here - what's the best way to add the blue or additional alerts without blowing up the system
# How do we efficiently compare 4+ dates?
# This is the gain from the hash instead of strings...

strHighDate = uwlibweb.getHighest(hashAlertDate)

for strKey,strValue in hashAlertDate.items():
    # Avoid posting a blank alert
    if (strValue == strHighDate) and (strValue != 0):
        strAlertColor = strKey
        strAlertStatus = 1

# if strAlertRedDate and strAlertOrangeDate:
    # strAlertStatus = uwlibweb.getHighest(strAlertRedDate, strAlertOrangeDate)
# elif strAlertRedDate:
    # strAlertStatus = 1
# elif strAlertOrangeDate:
    # strAlertStatus = 2

if strAlertStatus:
    # Do something interesting here
    #strAlertColor = ''
    
    # Ignoring if both dates ar the same
    # This is extremely wonky
    # if strAlertStatus == 1:
        # strAlert = strAlertRed;
        # strAlertColor = 'red';
    # elif strAlertStatus == 2:
        # strAlert = strAlertOrange;
        # strAlertColor = 'orange';

    # Set alert color based on file contents
    # What happens if the color fails?
    # the color should fail before we get here
    strStyle = 'uwalert_' + strAlertColor + '.css'        

    # Take newest item and display
    strTitle = strAlert.entries[0].title # don't trust encoding
    strLink = 'http://emergency.washington.edu/'
    strDesc = strAlert.entries[0].description # don't trust encoding
    #http://mail.python.org/pipermail/python-list/2004-August/275972.html
    strDate = strAlert.entries[0].date
    strParsedDate = strAlert.entries[0].date_parsed
    
    strFormatDate = datetime(strParsedDate.tm_year, strParsedDate.tm_mon, strParsedDate.tm_mday, strParsedDate.tm_hour, strParsedDate.tm_min, strParsedDate.tm_sec)

    strContent = strDesc[:180] + '... '

    if strDesc and strTitle:
        strContent += '<a href="' + strLink + '" title ="' + strTitle + '">More Info</a> &gt;&gt;'

    strHTMLContent = """
<div id="alertBox">
<div id="alertBoxText">
        <h1>Campus Alert:</h1>
        <p>%s</p>
    </div>
    <div id="clearer"></div>
</div> """ % (strContent)
        
    #strFormatDate.strftime("%A, %B %d"))        # Enable once server time is fixed on spokane
        
    strContent = """
document.write('<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/prototype.js"><\/script>' +
'<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/scriptaculous.js?load=effects"><\/script>');

document.write('<link href="http://depts.washington.edu/uweb/emergency/%s" rel="stylesheet" type="text\/css" \/>' +
    '<sty' + 'le type="text\/css"><!-- body { margin: 0; padding: 0; } --><\/style>');

// displayAlert - grab HTML to display message 
function displayAlert()
{
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
function displayAlert(strMode)
{
    // Does nothing useful - for error & warning prevention
}
    """

strOutput = strHeader + strContent + "\n";

try:
    strFileout = '/rc22/d10/uweb/public_html/emergency/alert.js'
    objFile = open(strFileout, "w")
    objFile.write(strOutput)
    objFile.close()
except Exception, strError:
    print "Error Writing to File %s because %s" % (strFileout, strError)
