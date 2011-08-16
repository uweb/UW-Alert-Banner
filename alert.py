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
        print 'Do Something'
