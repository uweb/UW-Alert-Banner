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
 * Include our javascript object script, the wonderful Prototype
 *---------------------------*/
document.write('<scr' + 'ipt type="text\/javascript" src="prototype.js"><\/script>');

function getMessage() {
		
	var sGetMsgUrl = 'get_message.php';
	new Ajax.PeriodicalUpdater('messageContainer', sGetMsgUrl, {
	    method: 'post', // using POST to combat IE caching,
	    frequency: 3,
	    
	});
	
	// output the HTML block we receive from the php script
	//document.write()

}