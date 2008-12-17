#!/usr/local/bin/python2.5

"""
Summary: script to run in cronjob - detect if there is something to post
if so, then output content to the alert.js file and include everything 
needed.  If no alert, then just output skeleton file.
"""

import os, re
import uwlibweb, feedparser
#import pprint
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

strTestHTMLContent = """
<div id="alertBox">
<div id="alertBoxText">
        <h1>Campus Alert:</h1>
        <p>There is no emergency.  For additional information, 
        please visit <a href="http://emergency.washington.edu">emergency.washington.edu</a></p>
    </div>
    <div id="clearer"></div>
</div> """

strAddElement = """
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
} """

###!!DEBUG!!###
####pp = pprint.PrettyPrinter(indent=4)####

# We want to make sure there are no problems with a lock of a post
# If there are any problems, just set the date to zero
hashAlert = dict() # {'red': '', 'orange': '', 'blue': '', 'steel': ''}
try:
    strFeed = feedparser.parse(uwlibweb.getFeedData(RED))
    strDate = uwlibweb.convertEpoch(strFeed.entries[0].date_parsed)
    hashAlert['red'] = {'feed': strFeed, 'date': strDate}
except:
    hashAlert['red'] = ''

try:
    strFeed = feedparser.parse(uwlibweb.getFeedData(ORANGE))
    strDate = uwlibweb.convertEpoch(strFeed.entries[0].date_parsed)
    hashAlert['orange'] = {'feed': strFeed, 'date': strDate}
except:
    hashAlert['orange'] = ''

try:
    strFeed = feedparser.parse(uwlibweb.getFeedData(BLUE))
    strDate = uwlibweb.convertEpoch(strFeed.entries[0].date_parsed)
    hashAlert['blue'] = {'feed': strFeed, 'date': strDate}
except:
    hashAlert['blue'] = ''

try:
    strFeed = feedparser.parse(uwlibweb.getFeedData(STEEL))
    strDate = uwlibweb.convertEpoch(strFeed.entries[0].date_parsed)
    hashAlert['steel'] = {'feed': strFeed, 'date': strDate}
except:
    hashAlert['steel'] = ''
    
#pp.pprint(hashAlert)    
    
# No alert is a good Alert
strAlertStatus = 0
################### StartWeird

hashDates = {}

for strKey,strValue in hashAlert.items():
    if strValue != '':
        for strKey2,strValue2 in hashAlert[strKey].items():
            hashDates[strKey] = hashAlert[strKey]['date']
        
# hashDates will only contain the colors with dates        
if hashDates:
    strHighDate = uwlibweb.getHighest(hashDates)
    for strKey,strValue in hashAlert.items():
        # Avoid posting a blank alert
        if hashAlert[strKey] != '':
            for strKey2,strValue2 in hashAlert[strKey].items():
                if hashAlert[strKey]['date'] == strHighDate:
                    strAlertColor = strKey
                    strAlertStatus = 1

strAlert = 0

if strAlertStatus:
    strAlert = hashAlert[strAlertColor]['feed']
################### End Weird

if strAlert:
    # A lack of color should fail before we get here
    # We are setting this value manually - we can trust it
    strStyle = 'uwalert_' + strAlertColor + '.css'

    # Take newest item and display
    strTitle = strAlert.entries[0].title.decode('iso-8859-1') # don't trust encoding
    strLink = 'http://emergency.washington.edu/'
    strDesc = strAlert.entries[0].description.decode('iso-8859-1') # don't trust encoding
    # Encode vs. Decode article
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
""" % (strStyle, re.escape(strHTMLContent))
    strOutput = strHeader + strContent + strAddElement + "\n";
else:
    strContent = """
function displayAlert(strMode)
{
    // Does nothing useful - for error & warning prevention
} """
    strOutput = strHeader + strContent + "\n";

# This may only be used for me - still good to have
strTestStyle = 'uwalert_steel.css'
strTestContent = """
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
""" % (strTestStyle, re.escape(strTestHTMLContent))

#uwlibweb.saveAlert('alert.js', strContent)
# Pushing out real alert
try:
    strFileout = '/rc22/d10/uweb/public_html/emergency/alert.js'
    objFile = open(strFileout, "w")
    objFile.write(strOutput)
    objFile.close()
except Exception, strError:
    print "Error Writing to File %s because %s" % (strFileout, strError)

# Alert for my test purposes 
strOutput = strHeader + strTestContent + strAddElement + "\n";
#uwlibweb.saveAlert('alert-test.js', strContent)
try:
    strFileout = '/rc22/d10/uweb/public_html/emergency/alert-test.js'
    objFile = open(strFileout, "w")
    objFile.write(strOutput)
    objFile.close()
except Exception, strError:
    print "Error Writing to File %s because %s" % (strFileout, strError)
