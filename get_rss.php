<?php
    /**
	 * Go get our alert content via an RSS feed out of the emergency blog
	 */
    require_once('Cache/Lite.php');

    // 4 & 6 are test categories
    // Alert Status (WP Categories)
    // 7 Publish
    // 8 — Red Alert 
    // 9 — Orange Alert    
    define('ORANGE', 4);
    define('RED', 6);
	
    // 1 * 60 * 60 == 3600;
    // Small performance hit?,
    // ------------------------------
    $options = array(
    'cacheDir' => 'rss_tmp/',
    'automaticSerialization' => TRUE,
    // Currently if the data is more than an hour old it won't display
    // May have evaluate later
    'lifeTime' => 3600 // 1 hour
    );

    // Create a Cache_Lite object
    $Cache_Lite = new Cache_Lite($options);

    require_once('lib.rss.php');

    $arrItemsRed = getFeedData(RED);
    $arrItemsOrange = getFeedData(ORANGE);
    
    // Actually could do a comparion against the cache in the lib.rss.php (getFeedData) method
    if ( $strStatus = getHighest($arrItemsRed[0]['pubDate'],$arrItemsOrange[0]['pubDate']) )
    {
        $intCategory = '';
        $strAlertColor = '';

        // Not taking into account if the dates are the same or if the objects passed are not dates
        if ($strStatus == 1)
        {
            $arrItems = $arrItemsRed;
            $strAlertColor = 'red';
            $intCategory = RED;
        }
        elseif ($strStatus == 2)
        {
            $arrItems = $arrItemsOrange;
            $strAlertColor = 'orange';
            $intCategory = ORANGE;
        }
        
        // Run through and find the latest version of content
        $arrCategoryCacheItems = $Cache_Lite->get('rss-cat-'.$intCategory);
        $arrMainCacheItems = $Cache_Lite->get('rss'.$intCategory);
        // Next!
        $arrItems = is_array($arrMainCacheItems) ? $arrMainCacheItems : $arrCategoryCacheItems;
        $strStatusCached = getHighest($arrCachedItems[0]['pubDate'],$arrItems[0]['pubDate']);
        
        setData($strAlertColor);
        
        // if the cached version is newer or the same age, then pull it
        if ($strStatusCached == 2)
            $Cache_Lite->save($arrItems,'rss');
    }
    else
    {
        // Clearing the cache by physically removing and all the file(s)
        // No Cache - No content
        $Cache_Lite->clean();
    }

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