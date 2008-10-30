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

var alert = '1';
var strStyle = alert ? 'uwalert_red.css' : 'uwalert_orange.css';
 
document.write('<scr' + 'ipt type="text\/javascript" src="prototype.js"><\/script>' +
'<link href="'+ strStyle +'" rel="stylesheet" type="text\/css" \/>' +
'<sty' + 'le type="text\/css"><!-- body { margin: 0px; } --><\/style>');

function addElement() {
  var body = document.getElementsByTagName('body')[0];
  
  var newdiv = document.createElement('div');
  var divIdName = 'alertMessage';
  
  newdiv.setAttribute('id',divIdName);
  //newdiv.innerHTML = 'Element Number '+num+' has been added! <a href=\'#\' onclick=\'removeElement('+divIdName+')\'>Remove the div "'+divIdName+'"</a>';
  body.appendChild(newdiv);
}

function get_cookie(cookie_name)
{
    var results = document.cookie.match ( '(^|;) ?' + cookie_name + '=([^;]*)(;|$)' );

    if ( results )
        return ( unescape ( results[2] ) );
    else
        return null;
}

function hideit(id)
{
    $('alertBox').hide();
    
    var cookie_date = new Date();
    var expdate = cookie_date.getTime();
    expdate += 3600*1000; //expires in 1 hour(milliseconds) 
    cookie_date.setTime(expdate);
    
    document.cookie = 'hide=yes;expires=' +
        cookie_date.toGMTString();

    // Dirty little Hack - need to find better solution before launch
    location.reload(true);
}

function getMessage(status)
{
    //var sGetMsgUrl = hide ? 'get_message.php?hide=1' : 'get_message.php';
    var sGetMsgUrl = 'get_message.php';
    
    var message = new Ajax.PeriodicalUpdater('alertMessage', sGetMsgUrl, {
	    method: 'post', // using POST to combat IE caching,
	    frequency: 10
	});
    
    if (status == 'stop')
    {
        message.stop();
    }
    else
    {
        message.start();
    }
    document.write(status);
    
    //return message;
}

function displayAlert()
{
    var hide = get_cookie("hide");
    if (hide)
    {
        addElement();
        getMessage('stop');
    }
    else
    {
        addElement();
        getMessage('start');
    }
}
// output the HTML block we receive from the php script
// if (!hide)
// {
    // document.write('<div id="alertMessage"><\/div>');
// }