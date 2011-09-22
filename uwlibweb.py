#!/bin/env python2.4

"""
Summary: Library containing functions for supporting the burner.py script
"""

import urllib, os, sys, time
from datetime import timedelta, datetime

def getJsonData():
    """getJsonData() - Get the data from the json api and save to a file
    """
    strURL = 'http://emergency.washington.edu/?json=1'
        
    strFileContents = readURL(strURL)

    strFilename = 'emergency.json'
    # Is there a reason to save every time?
    saveData(strFilename,strFileContents)
    
    return strFileContents

def getFeedData(intCategory):
    """getFeedData() - Get the data from the RSS feed and save to a file
    Mostly used for debugging - will find some use for it later
    """
    strURL = 'http://emergency.washington.edu/feed/?cat=' + str(intCategory)
        
    strFileContents = readURL(strURL)

    strFilename = 'emergency-' + str(intCategory) + '.rss'
    # Is there a reason to save every time?
    saveData(strFilename,strFileContents)
    
    return strFileContents

def convertEpoch(oDate):
    """Convert '2007-02-05 16:15:18' 
    To: '%Y-%m-%d %H:%M:%S' 
    Takes date as an object, not as a string
    """
    strDate = str(datetime(oDate.tm_year, oDate.tm_mon, oDate.tm_mday, oDate.tm_hour, oDate.tm_min, oDate.tm_sec))

    strPattern = '%Y-%m-%d %H:%M:%S'
    return int(time.mktime(time.strptime(strDate, strPattern)))
    
def getHighest(hashItems):
    """Guess what?  Returns the highest (value)
    Number in the hash 
    TODO: Either take a slide or modify to see HoH
    or the dict (...Python Equiv)
    """
    keys = hashItems.keys()
    keys.sort()
    arrItems = [hashItems[key] for key in keys]
    
    return arrItems[0]
 
def readURL(strURL):
    """Returns the contents from the URL
    """
    oFile = urllib.urlopen(strURL)
    strData = oFile.read()
    oFile.close()
    return strData
    
def saveAlert(strFilename, strAlertText):
    """Create actual js for usage
    Not in production yet
    """
    try:
        strFileout = 'storage/' + strFilename
        objFile = open(strFileout, "w")
        objFile.write(strAlertText)
        objFile.close()
    except Exception, strError:
        print "Error Writing to File %s because %s" % (strFileout, strError)
    
def saveData(strFilename, strFileContents):
    """Saves data to the storage location
    May opt to remove and only use for debug
    """
    strFolder = 'storage/'
    
    #save the data into the file
    try:
        oFile = open(strFolder + strFilename, 'w')
        oFile.write(strFileContents)
        oFile.close()
        return 1
    except Exception, strError:
        print "Error Writing to File %s%s because %s" % (strFolder, strFilename, strError)
