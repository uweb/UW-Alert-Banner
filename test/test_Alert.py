import sys, os
import unittest
import urllib2
sPath = os.getcwd()       
sys.path.append(sPath) 
from Alert import *

class TestAlert(unittest.TestCase):

    def setUp(self):
        self.Alert = Alert()
        self.Alert.load()

    def testload(self):
        self.assertEqual(self.Alert.code, 'MGH')
        self.assertEqual(self.Alert._cat, self.Alert.cat)

    def testdisplay(self):
        self.assertEqual(len(self.Alert._orgs), 0)

if __name__ == '__main__':
    ## unittest.TextTestRunner(verbosity=2).main())
    unittest.main()
