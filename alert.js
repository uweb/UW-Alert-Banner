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

// Might have to do some additional work here
document.write('<scr' + 'ipt type="text\/javascript" src="prototype.js"><\/script>');
document.write('<scr' + 'ipt type="text\/javascript" src="emergency.js"><\/script>');

// Dynamically set the next two
var alert = 'red';
var strStyle = alert == 'red' ? 'uwalert_red.css' : 'uwalert_orange.css';
document.write('<link href="'+ strStyle +'" rel="stylesheet" type="text\/css" \/>' +
'<sty' + 'le type="text\/css"><!-- body { margin: 0px; } --><\/style>');