#!/usr/bin/env python
""" 
CGI include for grabbing the json from wordpress.com
"""
import cgi
import urllib2

######################## DEBUG #############################
## import pdb
## import cgitb
## Necessary to print debug errors to display in browser
## cgitb.enable()
######################## DEBUG #############################

__author__ = "Chris Heiland"
__copyright__ = "Copyright 2012, University of Washington"
__credits__ = ["Chris Heiland"]
__license__ = "GPL"
__version__ = "0.5"
__maintainer__ = "Chris Heiland"
__email__ = "cheiland@uw.edu"
__status__ = "Development"

def main():
    """
    Main section for UW Head CGI Include.
    """

    strUrl = 'https://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish'

    oFile = urllib2.urlopen(strUrl,timeout=10)
    strJson = oFile.read().replace('\n', '')
    oFile.close()

    print "Content-type: text/html"
    print
    print strJson

if __name__ == "__main__":
    main()
