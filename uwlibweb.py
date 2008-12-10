#!/usr/local/bin/python2.5

"""
Summary: Library containing functions for supporting the burner.py script
"""

import urllib, os, sys
from datetime import timedelta, datetime

def getFeedData(intCategory):
    """getFeedData() - Get the data from the RSS feed and save to a file
    """
    strURL = 'http://emergency.washington.edu/?feed=rss2&cat=' + str(intCategory)
        
    strFileContents = readURL(strURL)

    strFilename = 'emergency-' + str(intCategory) + '.rss'
    # Is there a reason to save every time?
    saveData(strFilename,strFileContents)
    
    return strFileContents
    
def getHighest(oDate1, oDate2):
    """Returns the highest date between two dates
    Make sure to capture output with try / except block
    Unknown reason for failure
    """

    strDate1 = datetime(oDate1.tm_year, oDate1.tm_mon, oDate1.tm_mday, oDate1.tm_hour, oDate1.tm_min, oDate1.tm_sec)
    strDate2 = datetime(oDate2.tm_year, oDate2.tm_mon, oDate2.tm_mday, oDate2.tm_hour, oDate2.tm_min, oDate2.tm_sec)
    
    if strDate1 > strDate2:
        return 1
    elif strDate1 < strDate2:
        return 2
    elif strDate1 == strDate2:
        return 3
    else:
        return 0
        
def readURL(strURL):
    """Returns the contents from the URL
    """
    oFile = urllib.urlopen(strURL)
    strData = oFile.read()
    oFile.close()
    return str(strData)
    
def saveData(strFilename, strFileContents):
    """Saves data to the storage location
    May opt to remove and only use for debug
    """
    strFolder = '/rc22/d10/uweb/public_html/emergency/storage/'
    
    #save the data into the file
    try:
        oFile = open(strFolder + strFilename, 'w')
        oFile.write(strFileContents)
        oFile.close()
        return 1
    except Exception, strError:
        print "Error Writing to File %s%s because %s" % (strFolder, strFilename, strError)