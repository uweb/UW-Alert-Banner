<?php
    //require_once('get_rss.php'); // Take out to run as a cronjob
    require_once('Cache/Lite.php');
	/**
	 * Go get our alert content via an RSS feed out of the emergency blog
	 */
    
    // 1 * 60 * 60 == 3600;
    $options = array(
    'cacheDir' => 'rss_tmp/',
    'automaticSerialization' => TRUE,
    'lifeTime' => 3600 // 1 hour ?
    );

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
        <p><?php echo $strContent ?></p>
    </div>
    <a href="javascript:void(0)" onclick="javascript:hideit('alertBox');Effect.BlindUp('alertBox')">
    <img src="close.gif" name="xmark" width="10" height="10" id="xmark" /></a>
    <div id="clearer"></div>
</div>
<?php
    }
?>