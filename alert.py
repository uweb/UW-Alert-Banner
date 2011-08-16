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
        #self._header = ""
        #self._content = ""
        #self._footer = ""
        self._types = {
            '8' :'red',
            '9' :'orange',
            '10':'blue',
            '11':'steel'}

    def get_url(self):
        return "%s" % (self._url)
    def set_url(self, url):
        self._url = url
    def get_status(self):
        return "%s" % (self._status)
    def set_status(self, status):
        self._status = status
    def get_alert(self):
        return self._alert
    def set_alert(self, alert):
        self._alert = alert
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color

    color   = property(get_color, set_color)
    alert   = property(get_alert, set_alert)
    status  = property(get_status, set_status)
    url     = property(get_url, set_url)

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

        categories = self.alert['categories']

        ## If we can't find our type, then we're done
        for category in categories:
            if category['id'] in self._types:

        #if len(categories) == 1:
        #    category = categories[0] 
        #    self.color = self._types[category['id']]
        #else:


        ## TODO: Multiple categories????

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
            categories = self.alert['categories']
            for category in categories:

                if category['id'] == 5:
                    print """Title: %s""" % self.alert['title']
                    print """Excerpt: %s""" % self.alert['excerpt']
                    #print """Content: %s \n""" % self.alert['content']
        else:
            raise Exception("Problem with emergency feed")


    def display(self):
        print json.dumps(self.alertdata)

