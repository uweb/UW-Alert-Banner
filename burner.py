#!/bin/env python2.4

"""
Summary: script to run in cronjob - detect if there is something to post
if so, then output content to the alert.js file and include everything 
needed.  If no alert, then just output skeleton file.
"""

import os, re
import uwlibweb, feedparser
from datetime import timedelta, datetime

################ DEBUG ####################
#import pprint
#pp = pprint.PrettyPrinter(indent=4)
################ DEBUG ####################

strHeader = """
/*  University of Washington - Alert 1.0 Beta
 *  (c) 2008 Chris Heiland, Tim Chang-Miller
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
 *  	displayAlert();
 *  </script>
 *  </body>
 *  </html>
 *
 *--------------------------------------------------------------------------*/
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
STEEL = 11

# We want to make sure there are no problems with a lock of a post
# If there are any problems, just set the entry to zero
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

# No alert is a good Alert
strAlert = ''
strStyle = ''
################### Start Less Weird Than Yesterday

#Example Data Structure
# # # # hashAlert{
    # # # # 'color': {'feed': '', 'date', ''},
    # # # # 'color': {'feed': '', 'date', ''},
    # # # # 'color': {'feed': '', 'date', ''},
    # # # # 'color': {'feed': '', 'date', ''},
    # # # # }
    
hashDates = {}

for strKey,strValue in hashAlert.items():
    if strValue != '':
        hashDates[strKey] = hashAlert[strKey]['date']

#pp.pprint(hashDates)
#pp.pprint(hashAlert)

# hashDates will only contain the colors with dates        
if hashDates:
    strHighDate = uwlibweb.getHighest(hashDates)
    for strAlertColor,strValue in hashAlert.items():
        # Avoid posting a blank alert
        if strValue != '':
            if hashAlert[strAlertColor]['date'] == strHighDate:
                strAlert = hashAlert[strAlertColor]['feed']
                strStyle = 'uwalert_' + strAlertColor + '.css'

################### End Less Weird Than Yesterday

strPlainAlert = ''

if strAlert:

    # Take newest item and display
    strTitle = strAlert.entries[0].title.encode("iso-8859-15", "replace") # don't trust encoding
    strLink = 'http://emergency.washington.edu/'
    strDesc = strAlert.entries[0].description.encode("iso-8859-15", "replace") # don't trust encoding
    # Encode vs. Decode article
    #http://mail.python.org/pipermail/python-list/2004-August/275972.html
    strDate = strAlert.entries[0].date
    strParsedDate = strAlert.entries[0].date_parsed

    strFormatDate = datetime(strParsedDate.tm_year, strParsedDate.tm_mon, strParsedDate.tm_mday, strParsedDate.tm_hour, strParsedDate.tm_min, strParsedDate.tm_sec)

    if strDesc and strTitle:
        strPlainAlert = strTitle + ".\n" + "<break />\n" + strDesc +  '.'
        strContent = strDesc[:180] + '... '    
    else:
        strContent = 'Whoops'

    # This will come in handy once more alert types are displayed
    strAddElement = """
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
} """

#    strJSInclude = """
#    document.write('<scr' + 'ipt type="text\/javascript" src="http://emergency.washington.edu/prototype.js"><\/script>' +
#    '<scr' + 'ipt type="text\/javascript" src="http://emergency.washington.edu/scriptaculous.js?load=effects"><\/script>');
#    """

    strContent = """// Code contributed by Dustin Brewer
var strProto = (window.location.protocol == 'https:') ? 'https://' : 'http://';
var strCSS = document.createElement('link');
strCSS.setAttribute('href', strProto + 'emergency.washington.edu/%s');
strCSS.setAttribute('rel','stylesheet');
strCSS.setAttribute('type','text/css');
document.getElementsByTagName('head')[0].appendChild(strCSS);

// displayAlert - grab content to display message 
function displayAlert()
{
    var strAlertTitle = '%s';
    var strAlertLink = '%s';
    var strAlertMessage = '%s';
    
    addElement(strAlertTitle,strAlertLink,strAlertMessage);
}
""" % (strStyle, re.escape(strTitle), strLink, re.escape(strContent))

    strOutput = strHeader + strContent + strAddElement + "\n";
else:
    strContent = """
function displayAlert(strMode)
{
    // Does nothing useful - for error & warning prevention
} """
    strOutput = strHeader + strContent + "\n";

# Output all alerts and finish with the notification
uwlibweb.saveAlert('alert.js', strOutput)

uwlibweb.saveAlert('alert.txt', strPlainAlert)
