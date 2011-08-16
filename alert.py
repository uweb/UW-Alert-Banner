#!/bin/env python2.4

"""
Summary: UW Alert Banner System package
"""

######################################## DEBUG #################################
## import pdb; set_trace();
## import pdb
######################################## DEBUG #################################

__author__ = "Chris Heiland"
__copyright__ = "Copyright 2011, University of Washington"
__credits__ = ["Chris Heiland"]
__license__ = "GPL"
__version__ = "0.2"
__maintainer__ = "Chris Heiland"
__email__ = "cheiland@uw.edu"
__status__ = "Development"

import os, sys, time
import urllib2,json
from datetime import timedelta, datetime

class AlertBanner(object):
    """ 
    Primary Alert Object
    """
    def __init__(self):
        self._url = 'http://emergency.washington.edu/?json=1&count=1'
        self._cache = 'storage/'
        self._alertdata = ""
        self._filename = 'emergency.json'
        self._status = ""
        self._alert = ""
        self._color = ""
        self._content = ""
        self._output = ""
        self._types = {
            5  :'test',
            8  :'red',
            9  :'orange',
            10 :'blue',
            11 :'steel'}

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

    alert   = property(get_alert, set_alert)
    color   = property(get_color, set_color)
    output  = property(get_output, set_output)
    status  = property(get_status, set_status)
    url     = property(get_url, set_url)

    def _build(self):
        strHeader = """
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
         *  	displayAlert();
         *  </script>
         *  </body>
         *  </html>
         *
         *  Full docs at: 
         *  uw.edu/externalaffairs/uwmarketing/toolkits/uw-alert-banner/
         *
         *--------------------------------------------------------------------------*/
        """

        strAddElement = """// addElement - display HTML on page right below the body page
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

        self.output = strHeader + strContent + strAddElement + "\n"

        #else:
        #    strContent = """
        #function displayAlert(strMode)
        #{
        #    // Does nothing useful - for error & warning prevention
        #} """

        #    self.output = strHeader + strContent + "\n"

    def load(self):
        """
        Get the data from the json api and save to a file
        """
        oFile = urllib2.urlopen(self._url)
        self._alertdata = json.loads(oFile.read())
        oFile.close()

        ## The assumption is the latest post has our data
        self.status = self._alertdata['status']
        self.alert = self._alertdata['posts'][0]

        ## We only need to verify there is an alert color available
        for category in self.alert['categories']:
            ## If we can't find our type, then we're done
            if category['id'] in self._types:
                self.color = self._types[category['id']]

        # TODO: Is there a reason to save every time?
        self._save()

    def _save(self):
        """
        Saves data to the storage location
        May opt to remove and only use for debug
        """

        try:
            oFile = open(self._cache + self._filename, 'w')
            oFile.write(json.dumps(self._alertdata))
            oFile.close()
            return 1
        except Exception, strError:
            print "Error Writing to File %s%s because %s" % (self._cache, self._filename, strError)

    def _latest(self):
        """
        Grabs latest alert
        """
        if self.status == 'ok':
            if self.color:
                print """Title: %s""" % self.alert['title']
                print """Color: %s""" % self.color
                print """Excerpt: %s""" % self.alert['excerpt']
                #print """Content: %s \n""" % self.alert['content']
        else:
            raise Exception("Problem with emergency feed")


    def display(self):
        print json.dumps(self.alertdata)

