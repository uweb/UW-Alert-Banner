function getMessage()
{
    //var sGetMsgUrl = hide ? 'get_message.php?hide=1' : 'get_message.php';
    var sGetMsgUrl = 'get_message.php';
    
    var message = new Ajax.PeriodicalUpdater('alertMessage', sGetMsgUrl, {
	    method: 'post', // using POST to combat IE caching,
	    frequency: 3
	});

    var hide = get_cookie("hide");
    if (hide)
        message.stop();
    return message;
}

var oMessage = getMessage();

function addElement() 
{
  var body = document.getElementsByTagName('body')[0];
  
  var newdiv = document.createElement('div');
  var divIdName = 'alertMessage';
  
  newdiv.setAttribute('id',divIdName);
  
  body.insertBefore(newdiv, body.firstChild);
  //body.appendChild(newdiv);
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

    oMessage.stop();
}


function displayAlert()
{
    var hide = get_cookie("hide");
    
    if (hide)
    {
        oMessage.stop();
    }
    else
    {
        addElement();
        oMessage.start();
    }
}