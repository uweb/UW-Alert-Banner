<?php
    require_once('Cache/Lite.php');
    // If I take it out to run as a cronjob, then I must  put the cookie stuff here
    require_once('get_rss.php'); // Take out to run as a cronjob ?
    
	/**
	 * Go get our alert content via an RSS feed out of the emergency blog
	 */
    
    // 1 * 60 * 60 == 3600;
    $options = array(
    'cacheDir' => 'rss_tmp/',
    'automaticSerialization' => TRUE,
    'lifeTime' => 3600 // 1 hour ?
    );
   
    
    // Check if the cookie is set
    // We don't want to set a cookie every 3 seconds, but we want to know if it changes
    
    // Cookie has 3 possible states
    // - null
    // - Red
    // - Orange
   
    // This is the most redundant piece of code I have written to date
    // Based on get_rss running
    // $fh = fopen('emergency', 'r');
    // $strAlertColor = fread($fh, filesize('emergency'));
    // fclose($fh);

    // if ($_COOKIE['uwalertcolor'])
    // {
        // if ($_COOKIE['uwalertcolor'] != $strAlertColor)
        // {
            // // This might be an unnecessary step
            // setcookie( 'uwalertcolor' , $strAlertColor , time() - 1 );    
            // setcookie( 'uwalertcolor' , $strAlertColor , time()+60*60*24*1 );
        // }
    // }
    // else
    // {
        // setcookie( 'uwalertcolor' , $strAlertColor , time()+60*60*24*1 );
    // }
 
    
    // Create a Cache_Lite object
    $Cache_Lite = new Cache_Lite($options);
    
    // Grab the information created by the get_rss.php script
    $arrItems = $Cache_Lite->get('rss');
 
    // If something exists in the cache
    if ( is_array($arrItems) )
    {
        // Take newest item and display
        $strTitle = $arrItems[0]['title'];
        $strLink = $arrItems[0]['link'];
        $strDesc = $arrItems[0]['description'];
        $strPubdate = $arrItems[0]['pubDate'];

        // Content length unknown, trim to reasonable length
        $strContent = $strDesc." ";
        $strContent = substr($strContent,0,200);
        $strContent = substr($strContent,0,strrpos($strContent,' '));
        $strContent = $strContent."...";        
        
        $strContent = ($strLink) || ($strTitle) ? 
            $strContent . '<a href="' . $strLink . '" title ="'. $strTitle .'">More Info</a> &gt;&gt;' 
            : '';
    }

    /**
           * HTML goes here
           */
    // If there is an RSS feed to pull
    if ($strContent)
    {
?>
<div id="alertBox">
    <div id="alertBoxText">
        <h1>Campus Alert:</h1>
        <p><?php echo $strContent ?> <span>(<?php echo $strPubdate?>)</span></p>
    </div>
    <a href="javascript:void(0)" onclick="javascript:hideit('alertBox');Effect.BlindUp('alertBox')">
    <img src="http://depts.washington.edu/uweb/emergency/close.gif" name="xmark" width="10" height="10" id="xmark" /></a>
    <div id="clearer"></div>
</div>
<?php
    }
?>