<?php
    require_once('Cache/Lite.php');
	/**
	 * Go get our alert content via an RSS feed out of the emergency blog
	 */
    
    // 1 * 60 * 60 == 3600;
    $options = array(
    'cacheDir' => 'rss_tmp/',
    'lifeTime' => 3600 // 1 hour ?
    );

    // Create a Cache_Lite object
    $Cache_Lite = new Cache_Lite($options);

    $arrItems = $Cache_Lite->get('rss');
    
    // Alert Status (WP Categories)
    // 7 Publish
    // 9 — Orange Alert
    // 8 — Red Alert 

    if (!$arrItems)
    {
        require_once('lib.rss.php');
        //$arrItems7 = getFeedData(7); // Don't think we need this 
        $arrItems8 = getFeedData(6);
        $arrItems9 = getFeedData(4);
        
        $strStatus = getHighest($arrItems8[0]['pubDate'],$arrItems9[0]['pubDate']);

        // Not taking into account if the dates are the same or if the objects passed are not dates
        if ($strStatus == 1)
            $arrItems = $arrItems8;
        elseif ($strStatus == 2)
            $arrItems = $arrItems9;
            
        $Cache_Lite->save($arrItems);
    }

    // Take newest item and display
    $strTitle = $arrItems[0]['title'];
    $strLink = $arrItems[0]['link'];
    $strDesc = $arrItems[0]['description'];
    //$strDate = $arrItems[0]['pubDate']; // Compare to current date ?

    // Content length unknown, trim to reasonable length
    $strContent = $strDesc." ";
    $strContent = substr($strContent,0,250);
    $strContent = substr($strContent,0,strrpos($strContent,' '));
    $strContent = $strContent."...";
    
    /**
           * HTML goes here
           */
    $strContent .= '<a href="' . $strLink . '" title ="'. $strTitle .'">More Info</a> &gt;&gt;';
    
    // New Content After a Long Period
    // New Content After a Short Period - What is a short period? 5 sec, 5 minutes?  How to avoid overload...
    // Clear Content After None Available

    // if rss feed exists
        // if new
            // then cache
        // else
            // then grab from cache
    // else
        // make note, check again in time 
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
