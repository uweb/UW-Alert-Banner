#!/usr/bin/env python2.6

import urllib2, json
from alert import AlertBanner

#strURL = 'http://emergency.washington.edu/?json=1'
#oFile = urllib2.urlopen(strURL)
#oJ = json.loads( oFile.read() )

#for post in oJ['posts']:
#    for category in post['categories']:
#        print category['id']

#strURL = 'http://emergency.washington.edu/category/emergency-links/?json=1'
#strURL = 'http://emergency.washington.edu/api/get_category_posts/?id=8' 
##oFile = urllib2.urlopen(strURL)
##oJ = json.loads( oFile.read() )
##
##print json.dumps( oJ, sort_keys=True, indent=4) 
#print oJ['pages']

alert = AlertBanner()

alert.load()
alert._latest()
