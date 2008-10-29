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
document.write('<scr' + 'ipt type="text\/javascript" src="prototype.js"><\/script>' +
'<link href="uwalert_red.css" rel="stylesheet" type="text\/css" \/>' +
'<sty' + 'le type="text\/css"><!-- body { margin: 0px; } --><\/style>');

function hideit(id)
{
    $('alertBox').hide();

    var sGetMsgUrl = 'get_message.php?hide=1';
}

function getMessage() {
		
	var sGetMsgUrl = 'get_message.php';
	new Ajax.PeriodicalUpdater('alertMessage', sGetMsgUrl, {
	    method: 'post', // using POST to combat IE caching,
	    frequency: 3,
	});
	
	// output the HTML block we receive from the php script
	document.write('<div id="alertMessage"><\/div>');

}