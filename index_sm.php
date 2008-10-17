<html>
<head>
    <title>UW Content</title>
    <link href="uwalert_red.css" rel="stylesheet" type="text/css" />
    <style type="text/css">
        <!-- body { margin: 0px; } -->
    </style>
    
    <script type="text/javascript" src="prototype.js"></script>
    
    <script type="text/javascript">
		
		function getMessage() {
		
			var sGetMsgUrl = 'get_message.php';
			new Ajax.PeriodicalUpdater('MessageContainer', sGetMsgUrl, {
			    method: 'post', // using POST to combat IE caching,
			    frequency: 3,
			    
			});
		
		}
       
    </script>
    
</head>
<body>

<script type="text/javascript">
	getMessage();
</script>

<div id="MessageContainer"></div>

</body>
</html>