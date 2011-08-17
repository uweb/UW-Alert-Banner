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
        oFile = open('storage/emergency.json', 'r')
        strData = json.loads(oFile.read())
        oFile.close()

        self.assertEqual(self.banner.status, 'ok')
        self.assertEqual(self.banner.color, 'red')
        self.assertEqual(self.banner._alertdata, strData)

    def testdisplay(self):
        self.assertEqual(self.banner.display('plain'),"Incoming Asteroid.\n<break />\nDESC: Astroid Fatal.")
        self.assertEqual(self.banner.display(),"""\n        /*  University of Washington - Alert 2.0 Beta\n         *  (c) 2011 Chris Heiland, Tim Chang-Miller\n         *\n         *  Script should be included like such:\n         *  \n         *  <html>\n         *  <head>\n         *  <title>Page Title</title>\n         *  <script type="text/javascript" src="http://emergency.washington.edu/alert.js"></script>\n         *  </head>\n         *  <body>\n         *  \n         *  <script type="text/javascript">\n         *  \tdisplayAlert();\n         *  </script>\n         *  </body>\n         *  </html>\n         *\n         *  Full docs at: \n         *  uw.edu/externalaffairs/uwmarketing/toolkits/uw-alert-banner/\n         *\n         *--------------------------------------------------------------------------*/\n        // Code contributed by Dustin Brewer\n                var strProto = (window.location.protocol == \'https:\') ? \'https://\' : \'http://\';\n                var strCSS = document.createElement(\'link\');\n                strCSS.setAttribute(\'href\', strProto + \'emergency.washington.edu/uwalert_red.css\');\n                strCSS.setAttribute(\'rel\',\'stylesheet\');\n                strCSS.setAttribute(\'type\',\'text/css\');\n                document.getElementsByTagName(\'head\')[0].appendChild(strCSS);\n\n                // displayAlert - grab content to display message \n                function displayAlert()\n                {\n                    var strAlertTitle = \'Incoming\\ Asteroid\';\n                    var strAlertLink = \'http://emergency.washington.edu/\';\n                    var strAlertMessage = \'There\\\'s\\ no\\ hope\\,\\ classes\\ cancelled\';\n                    \n                    addElement(strAlertTitle,strAlertLink,strAlertMessage);\n                }\n                // addElement - display HTML on page right below the body page\n        // don\'t want the alert to show up randomly\n        function addElement(strAlertTitle,strAlertLink,strAlertMessage)\n        {\n          // Grab the tag to start the party\n          var bodyTag = document.getElementsByTagName(\'body\')[0];\n          \n          bodyTag.style.margin = \'0px\';\n          bodyTag.style.padding = \'0px\';\n\n          var wrapperDiv = document.createElement(\'div\');\n          wrapperDiv.setAttribute(\'id\',\'alertMessage\');\n\n          var alertBoxDiv = document.createElement(\'div\');\n          alertBoxDiv.setAttribute(\'id\', \'alertBox\');\n\n          var alertBoxTextDiv = document.createElement(\'div\');\n          alertBoxTextDiv.setAttribute(\'id\', \'alertBoxText\');\n          \n          var header1 = document.createElement(\'h1\');\n          var header1Text = document.createTextNode(\'Campus Alert:\');\n          header1.appendChild(header1Text);\n\n          var alertTextP = document.createElement(\'p\');\n          var alertText = document.createTextNode(strAlertMessage);\n          alertTextP.appendChild(alertText);\n\n          var alertLink = document.createElement(\'a\');\n          alertLink.setAttribute(\'href\', strAlertLink);\n          alertLink.setAttribute(\'title\', strAlertTitle);\n          var alertLinkText = document.createTextNode(\'More Info\');\n          alertLink.appendChild(alertLinkText);\n\n          var gtText = document.createTextNode(\' >>\');\n          \n          var clearDiv = document.createElement(\'div\');\n          clearDiv.setAttribute(\'id\', \'clearer\');\n\n          // Start Building the Actual Div\n          alertTextP.appendChild(alertLink);\n          alertTextP.appendChild(gtText);\n\n          alertBoxTextDiv.appendChild(header1);\n          alertBoxTextDiv.appendChild(alertTextP);\n\n          alertBoxDiv.appendChild(alertBoxTextDiv);\n          alertBoxDiv.appendChild(clearDiv);\n\n          wrapperDiv.appendChild(alertBoxDiv);\n          \n          bodyTag.insertBefore(wrapperDiv, bodyTag.firstChild);\n        } \n""")

if __name__ == '__main__':
    ## unittest.TextTestRunner(verbosity=2).main())
    unittest.main()
