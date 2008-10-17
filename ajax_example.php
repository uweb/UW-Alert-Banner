<html>
<head>
    <title>UW Content</title>
    <link href="uwalert_red.css" rel="stylesheet" type="text/css" />
    <style type="text/css">
        <!-- body { margin: 0px; } -->
    </style>
    <script type="text/javascript" src="prototype.js"></script>
    
    <script type="text/javascript">
    
    	new Ajax.Request('get_message.php',
		  {
		    method:'get',
		    onSuccess: function(transport){
		      var response = transport.responseText || "no response text";
		      alert("Success! \n\n" + response);
		    },
		    onFailure: function(){ alert('Something went wrong...') }
		  });
       
    </script>    
    
</head>
<body>

</body>
</html>