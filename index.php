<html>
<head>
<title>UW Content</title>
<link href="uwalert_red.css" rel="stylesheet" type="text/css" />
<style type="text/css">
<!--
body {
	margin-left: 0px;
	margin-top: 0px;
	margin-right: 0px;
	margin-bottom: 0px;
}

-->
</style>

<script type="text/javascript" src="translator.js"></script>

<script type="text/javascript">

function addToStart() {

	// first we create a new div with document.createElement()
	var newcontent = document.createElement('div');

	// then we create some text with document.createTextNode()
	var newtext = document.createTextNode('Hello World!');

	// then we put the text in the div
	newcontent.appendChild(newtext);

	// and you can nest/combine them like this to add more text
	newcontent.appendChild(document.createTextNode('  It looks like a nice day!'));

	// then we want to get a reference to the body tag with document.getElementsByTagName()
	// this returns an array, so we only take the first result by specifying the [0] at the end
	var bodytag = document.getElementsByTagName('body')[0];

	// now we want to append 'newcontent' to 'bodytag' -- but not at the end
	// to prepend (insert at the beginning) we need to 'insert before' the 'first child' of the body tag
	// we do this by using the DOM's .insertBefore() method and .firstChild property:
	bodytag.insertBefore(newcontent,bodytag.firstChild);

}

</script>
<script type="text/javascript">
function hide(id)
{
	el = document.getElementById(id);
	el.style.display = 'none';
}
</script>

</head>
<body>
<?php //<script type="text/javascript">addToStart()</script> ?>
<?php 
    include_once('rss_php.php');
    $RSS_PHP = new rss_php; 
    $RSS_PHP->load('http://emergency.washington.edu/?feed=rss2&cat=4');

    $arrItems = $RSS_PHP->getItems();
    
    //var_dump($arrItems);
    $strTitle = $arrItems[0]['title'];
    $strLink = $arrItems[0]['link'];
    $strDesc = $arrItems[0]['description'];
?>

<div id="alertBox">
    <div id="alertBoxText">
        <h1>Campus Alert:</h1>   
        <p><?php echo $strDesc ?><a href="<?php echo $strLink ?>">More Info</a> &gt;&gt;  </p>
    </div>
  
    <a href="#" onclick="javascript:hide('alertBox')" border="0"><img src="close.gif" name="xmark" width="10" height="10" id="xmark" /></a>
    <div id="clearer"></div> 
</div>


<p>Content Below</p>
<script>
    try {readRSS(unescape("http://emergency.washington.edu/?feed=rss2&cat=4"),1);}
    catch(e) {}
</script>

</body>
</html>
<?php
//http://rssphp.net/documentation/v1/#RSS_PHP.Properties
?>