#!/usr/bin/env python

"""
Summary: script to run in cronjob - detect if there is something to post
if so, then output content to the alert.js file and include everything 
needed.  If no alert, then just output skeleton file.
"""

strHeader = """
/*  University of Washington - Alert 1.0 Beta
 *  (c) 2008 Chris Heiland, Tim Chang-Miller
 *
 *  Script should be included like such:
 *  
 *  <html>
 *  <head>
 *  <title>Page Title</title>
 *  <script type="text/javascript" src="http://depts.washington.edu/uweb/scripts/alert.js"></script>
 *  </head>
 *  <body>
 *  
 *  <script type="text/javascript">
 *  	getMessage();
 *  </script>
 *  </body>
 *  </html>
 *
 *--------------------------------------------------------------------------*/

/*
 * Include our javascript object script, the wonderful Prototype... and friends
 *---------------------------*/
 """;

#        var strStyle = strAlertColor == 'red' ? 'uwalert_red.css' : 'uwalert_orange.css';
strAlertColor = 'color of alert'; # TODO: Open  emergency file and pull color

if (data exists)
{
    strContent = """
        // If the file does not exist - then don't show
        document.write('<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/prototype.js"><\/script>' +
        '<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/scriptaculous.js?load=effects"><\/script>' +
        '<scr' + 'ipt type="text\/javascript" src="http://depts.washington.edu/uweb/emergency/emergency.js"><\/script>');
        
        document.write('<link href="http://depts.washington.edu/uweb/emergency/%s" rel="stylesheet" type="text\/css" \/>' +
        '<sty' + 'le type="text\/css"><!-- body { margin: 0; padding: 0; } --><\/style>');
    """;
    
    print strContent, %s; # print to or save to a variable
}
else
{
    strContent = """
        function displayAlert()
        {
            // Does nothing - for error prevention
        }   
    """
}

strOutput = strHeader + strContent;

print strOutput to alert.js