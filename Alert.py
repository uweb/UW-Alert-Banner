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

class Alert(object):
    """ 
    Primary Alert Object
    """
    def __init__(self):
        self._url = 'http://emergency.washington.edu/?json=1'
        self._cache = 'storage/'
        self._alertdata = ""
        self._filename = 'emergency.json'
        self._header = ""
        self._content = ""
        self._footer = ""

    def load(self):
        """
        Get the data from the json api and save to a file
        """
        oFile = urllib.urlopen(self._url)
        self._alertdata = oFile.read()
        oFile.close()

        # TODO: Is there a reason to save every time?
        self._save()

    def _save(self):
        """
        Saves data to the storage location
        May opt to remove and only use for debug
        """

        try:
            oFile = open(self._cache + self._filename, 'w')
            oFile.write(self._alertdata)
            oFile.close()
            return 1
        except Exception, strError:
            print "Error Writing to File %s%s because %s" % (self._cache, self._filename, strError)

