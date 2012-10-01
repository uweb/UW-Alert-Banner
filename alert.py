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
        self._url = 'http://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish'
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

def main():
    """
    Main section for UW Alert Banner
    """

    banner = AlertBanner()
    banner.display()

if __name__ == "__main__":
    main()
