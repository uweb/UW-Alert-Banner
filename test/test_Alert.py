import sys, os
import xml.dom.minidom
import unittest
import urllib
sPath = os.getcwd()       
sys.path.append(sPath) 
from burner import *

class TestAlert(unittest.TestCase):

    def setUp(self):
        self.Alert = Alert()
        self.Alert.load()

    def testload(self):
        self.assertEqual(self.Alert.code, 'MGH')
        self.assertEqual(self.Alert._cat, self.Alert.cat)

    def testaddsingle(self):
        oOrg = Organization()
        oOrg.name = ('Something & Testing')
        oOrg.url = ('http://www.washington.edu/')
        self.Alert.add((oOrg,))
        self.assertEqual(len(self.Alert._orgs), 1)

    def testaddmulti(self):
        oOrg1 = Organization()
        oOrg1.name = ('Something & Testing 1')
        oOrg1.url = ('http://www.washington.edu/')
        oOrg2 = Organization()
        oOrg2.name = ('Something Testing 2')
        oOrg2.url = ('http://www.washington.edu/')
        oOrg2.cat = ('food')
        self.Alert.add(oOrg1)
        self.Alert.add(oOrg2)
        self.assertEqual(len(self.Alert._orgs), 2)

    def testaddnone(self):
        self.assertEqual(len(self.Alert._orgs), 0)

if __name__ == '__main__':
    ## unittest.TextTestRunner(verbosity=2).main())
    unittest.main()
