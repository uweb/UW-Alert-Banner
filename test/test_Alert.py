import sys, os
import unittest
import urllib2,json
sPath = os.getcwd()       
sys.path.append(sPath) 
from alert import AlertBanner

class TestAlertBanner(unittest.TestCase):

    def setUp(self):
        self.banner = AlertBanner()
        self.banner.url = 'http://emergency.washington.edu/emergency.json'
        self.banner.load()

    def testload(self):
        ## For consistent tests, we have red alert
        oFile = open('test/emergency.json', 'r')
        strData = json.loads(oFile.read())
        oFile.close()

        self.assertEqual(self.banner.status, 'ok')
        self.assertEqual(self.banner.color, 'red')
        self.assertEqual(self.banner._alertdata, strData)

    def testdisplay(self):
        self.assertEqual(self.banner.display('plain'),"Incoming Asteroid.\n<break />\nDESC: Astroid Fatal.")
        ### Prod Banner
        oFile = open('test/alert.js', 'r')
        strData = oFile.read()
        oFile.close()
        self.assertEqual(self.banner.display(),strData)

if __name__ == '__main__':
    ## unittest.TextTestRunner(verbosity=2).main())
    unittest.main()
