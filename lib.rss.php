<?php
    // getFeedData - grab the RSS feed from the category and 
    // put it into an array
    function getFeedData($intCategory)
    {
        // Remember this function is called twice
        require_once('Cache/Lite.php');
        $options = array(
            'cacheDir' => 'rss_tmp/',
            'automaticSerialization' => TRUE,
            'lifeTime' => 3600 // 1 hour ?
        );
        $Cache_Lite = new Cache_Lite($options);
        require_once('rss_php.php');
        $RSS_PHP = new rss_php;
        
        $strURL = 'http://emergency.washington.edu/?feed=rss2&cat=' .
            $intCategory;

        $RSS_PHP->load($strURL);

        $arrItems = $RSS_PHP->getItems();
        
        // If the fetch was sucessfull, save to cache
        // otherwise, grab from prior cache
        // This is a test if the site is available or not
        
        // this fails if the server dies before it can initially create a cache
        // this may not be a big problem
        
        if ( is_array($arrItems) )
            $strStatus = $Cache_Lite->save($arrItems,'rss-cat-'.$intCategory);
        else
            $arrItems = $Cache_Lite->get('rss-cat-'.$intCategory);
        
        // Array will always load newest to oldest
        return $arrItems;
    }
    
    // getHighest - return the highest date, if fail for any reason
    // return 0 - failure includes both dates matching
    function getHighest($strDate1, $strDate2)
    {
        // This should work in theory
        // Aparently this does not work, needs information split
        //if (!checkdate($strDate1) || !checkdate($strDate2))
            //return 0;

        $strDate1 = strtotime($strDate1);
        $strDate2 = strtotime($strDate2);
        
        if ($strDate1 > $strDate2)
            return 1;
        elseif ($strDate1 < $strDate2)
            return 2;
        else
            return 0;
    }
    
    // The next three functions provide the javascript portion of the script
    // To see if we need to signal the decay or if we have new data
    // Could make a class out of this if I get really bored
    
    // setData - Saving RSS data
    // Linked to rmData function
    function setData($strData)
    {
        $fh = fopen('emergency', 'w');
        fwrite($fh, $strData); // Should have an or die here
        fclose($fh);
    }

    // rmData - Removing saved RSS data
    // Linked to saveData function
    // Takes no arguements
    function rmData()
    {
        if (file_exists('emergency'))
            unlink('emergency');
    }
?>