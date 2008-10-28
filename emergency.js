        function hide(id)
        {
        	el = document.getElementById(id);
        	el.style.display = 'none';
        }
		
        function getMessage()
        {
			var sGetMsgUrl = 'get_message.php';
			new Ajax.PeriodicalUpdater('MessageContainer', sGetMsgUrl, {
			    method: 'post', // using POST to combat IE caching,
			    frequency: 3,
			});
            
			document.write('<div id="alertBox"><div id="alertBoxText"><h1>Campus Alert:</h1><p id="MessageContainer"></p></div><img src="close.gif" name="xmark" width="10" height="10" id="xmark" /><div id="clearer"></div></div>');
		
		}