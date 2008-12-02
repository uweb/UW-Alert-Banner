<?php
// Summary - Get or Create Cached RSS Data - run via CronJob (5 - 15min increments)

    //require_once('Cache/Lite.php');
	/**
	 * Go get our alert content via an RSS feed out of the emergency blog
	 */
    
    // 1 * 60 * 60 == 3600;
    // Small performance hit, may want te re-eval later
    // Could Eliminate Cache Altogether if needed
    // Then take advantage of the saveData/rmData more
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

    // 4 & 6 are test categories
    
    // Alert Status (WP Categories)
    // 7 Publish
    // 8 — Red Alert 
    // 9 — Orange Alert

    require_once('lib.rss.php');
    //$arrItems7 = getFeedData(7); // Don't think we need this 

    // Need a way of detecting if no items are available
    // Could make the getHigest a bit more robust, or feed it 
    
    // More login - need to remember this entire script is run 
    // every 10 seconds or less, maybe fork out another process
    // or have this run as a seperate script and have the 
    // get-message just pull from a file and have something run
    // as a cronjob, not as fast, but we aren't going for speed here
    // Reliability is much more important than how fast they get the message
    $arrItemsRed = getFeedData(6);
    $arrItemsOrange = getFeedData(4);
    $strCookStatus1 = '';
    $strCookStatus2 = '';

    // Where is the check if the file doesn't change - if it stays the same - then we don't want to rewrite the cache
    if ( $strStatus = getHighest($arrItemsRed[0]['pubDate'],$arrItemsOrange[0]['pubDate']) )
    {
        $strAlertColor = '';

        // Not taking into account if the dates are the same or if the objects passed are not dates
        if ($strStatus == 1)
        {
            $arrItems = $arrItemsRed;
            $strAlertColor = 'red';
        }
        elseif ($strStatus == 2)
        {
            $arrItems = $arrItemsOrange;
            $strAlertColor = 'orange';
        }

        // Could replace this with another method and forgo traditinal caching
        // I don't think it's gaining us much at this point
        // As the RSS feed is updated every 5 minutes or so, it will probably
        // end up being more of a stumbling block than anything else
        $status = $Cache_Lite->save($arrItems,'rss');
        setData($strAlertColor); // We are touching the file
        //$strCookStatus1 = setcookie( 'uwalertcolor' , $strAlertColor , time()+60*60*24*1 , '/', '.washington.edu');
        // echo "Cache Creation Status: $status\n";
    }
    else
    {
        // If we are here that means there are no items to grab - clean the cache and
        // signal the decay
        
        // If we are here that also means the site could be down
        // If the site is down during an emergency or if it can't 
        // contact the site do we have bigger problems?
        
        // Worse case is the site is down and I need a way
        // to manually override it - but as of right now the site
        // would have to go down in the middle of an emergency to pose
        // much of a problem - is this really an issue?
        
        //$strCookStatus2 = setcookie( 'uwalertcolor' , $strAlertColor , time() - 1 );    
        
        // only remove data if it exists
        rmData();
        // Clearing the cache does physically remove all the file(s)
        $Cache_Lite->clean();
    }

    // New Content After a Long Period
    // New Content After a Short Period - What is a short period? 5 sec, 5 minutes?  How to avoid overload...
    // Clear Content After None Available - How long should content be available prior to clear?  1 day?  When
    // the event is over, how will we know?  Automatically clear vs manually clear
    // Manually Clear if the event is pulled from the Publish or any of the Sub Categories

    // if rss feed exists
        // if new
            // then cache
        // else
            // then grab from cache
    // else
        // make note, check again in time 
    // Save the Content for the RSS Feed
    
    // This should work... May not need this 
    // or at least change the way we need it
    // if ($strContent)
        // saveData($strContent);
    // else
        // rmData();
?>