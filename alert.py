#!/usr/bin/env python2.6

"""
Summary: UW Alert Banner System package
"""

__author__ = "Chris Heiland"
__copyright__ = "Copyright 2011, University of Washington"
__credits__ = ["Chris Heiland"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Chris Heiland"
__email__ = "cheiland@uw.edu"
__status__ = "Development"

import os, sys, time
import re
import urllib2, json
from datetime import timedelta, datetime

class AlertBanner(object):
    """ 
    Primary Alert Object
    """
    def __init__(self):
        self._url = 'https://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish'
        self._alertdata = ""
        self._status = ""
        self._alert = ""
        self._excerpt = ""
        self._color = ""
        self._link = 'http://emergency.washington.edu/'
        self._deploy = os.path.dirname( os.path.realpath( __file__ ) )+'/storage/'
        self._filename = 'alert'
        self._output = ""
        self._types = {
            'red-alert-urgent' : 'uwalert-red',
            'orange-alert'     : 'uwalert-orange',
            'steel-alert-fyis' : 'uwalert-steel'}

    def get_url(self):
        return "%s" % (self._url)
    def set_url(self, url):
        self._url = url
    def get_status(self):
        return "%s" % self._status
    def set_status(self, status):
        self._status = status
    def get_alert(self):
        return self._alert
    def set_alert(self, alert):
        self._alert = alert
    def get_color(self):
        return "%s" % self._color
    def set_color(self, color):
        self._color = color
    def get_output(self):
        return "%s" % self._output
    def set_output(self, output):
        self._output = output
    def get_excerpt(self):
        return "%s" % self._excerpt
    def set_excerpt(self, excerpt):
        self._excerpt = excerpt

    alert     = property(get_alert, set_alert)
    color     = property(get_color, set_color)
    excerpt   = property(get_excerpt, set_excerpt)
    output    = property(get_output, set_output)
    status    = property(get_status, set_status)
    url       = property(get_url, set_url)

    def load(self):
        """
        Get the data from the json api and save to a file
        """
        oFile = urllib2.urlopen(self._url,timeout=10)
        self._alertdata = json.loads(oFile.read().replace('\n', ''))
        oFile.close()

        count = self._alertdata['found'];

        if count > 0:
            self.alert = self._alertdata['posts'][0]

            ## We only need to verify there is an alert color available
            for strCatTitle, category in self.alert['categories'].iteritems():
                ## If we can't find our type, then we're done
                if category['slug'] in self._types:
                    self.color = self._types[category['slug']]

            if self.alert['excerpt']:
                arrWords = self.alert['excerpt'].split()
            else:
                arrWords = self.alert['content'].split()

            if len(arrWords) <= '35':
                excerpt = ' '.join(arrWords)
                self._excerpt = '%s '.decode('ascii') % excerpt
            else:
                excerpt = ' '.join(arrWords[:35])
                self._excerpt = '%s [...] '.decode('ascii') % excerpt

            # TODO: Is there a reason to save every time?
            #self._save(json.dumps(self._alertdata, sort_keys=True, indent=4),'alert.json')

    def _build(self):
        ## If we have an color, we are running an alert - we need
        ## this to be as streamlined as possible

        strHeader = """/*  University of Washington - Alert 2.0 Beta
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
"""

        if self.color:
            strContent = """// Code contributed by Dustin Brewer
var strProto = (window.location.protocol == 'https:') ? 'https://' : 'http://';
var strCSS = document.createElement('link');
strCSS.setAttribute('href', strProto + 'emergency.washington.edu/uwalert.css');
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
  alertBoxDiv.setAttribute('class', '%s');

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
    var strAlertTitle = '%s';
    var strAlertLink = '%s';
    var strAlertMessage = '%s';

    addElement(strAlertTitle,strAlertLink,strAlertMessage);
}
""" % (self.color, re.escape(self.alert['title']), self._link, re.escape(self._excerpt))
        else:
            strContent = """function displayAlert(strMode)
{
    // Does nothing useful (for error & warning prevention)
}
"""
        self.output = strHeader + strContent
        return 1

    def _save(self,sData,sFile):
        """
        Private method to save data to the storage/output locations
        """

        strLocation = """%s%s""" % (self._deploy,sFile)

        try:
            oFile = open(strLocation, 'w')
            oFile.write(sData)
            oFile.close()
            return 1
        except Exception, strError:
            print "Error Writing to File %s because %s" % (strLocation, strError)

    ## TODO: Needs more thought
    def display(self,sType=None):
        """
        Display latest alert in both plain and js mode
        """
        self.load()

        strPlain = ''
        if self.color:
            ## Plain text version requested by a department
            strPlain = """%s.\n<break />\n%s""" % (self.alert['title'],self._excerpt)

        self._save(strPlain,"""%s.txt""" % self._filename)
        ## Exists solely for tests
        if sType == 'plain':
            return strPlain

        ## if self._build():
        ##     self._save(self.output,"""%s.js""" % self._filename)
        ##     return self.output
        ## else:
        ##     print "Problem rendering banner\n"

def main():
    """
    Main section for UW Alert Banner
    """

    banner = AlertBanner()
    banner.display()

if __name__ == "__main__":
    main()
