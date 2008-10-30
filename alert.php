<?php
    $red = 1;
    
    $strStyle = $red ? 'uwalert_red.css' : 'uwalert_orange.css';

    echo "var sGetMsgUrlHide = '';";
     
    echo "document.write('<scr' + 'ipt type=\"text\/javascript\" src=\"prototype.js\"><\/script>" .
    "<link href=\"". $strStyle ."\" rel=\"stylesheet\" type=\"text\/css\" \/>" .
    "<sty' + 'le type=\"text\/css\"><!-- body { margin: 0px; } --><\/style>');";

    // Do some action here
    echo "
    function hideit(id)
    {
        $('alertBox').hide();
        new Ajax.Request('/get_message.php?hide=1');
    }";

    echo "
    function getMessage()
    {
            
        var sGetMsgUrl = 'get_message.php';
    	new Ajax.PeriodicalUpdater('alertMessage', sGetMsgUrl, {
    	    method: 'post', // using POST to combat IE caching,
    	    frequency: 3,
    	});
    	
    	// output the HTML block we receive from the php script
        if (sGetMsgUrlHide == '')
        {
            document.write('<div id=\"alertMessage\"><\/div>');
        }

    }";
?>