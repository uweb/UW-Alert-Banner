<?php

    // getFeedData - grab the RSS feed from the category and 
    // put it into an array
    function getFeedData($intCategory)
    {
        require_once('rss_php.php');
        $RSS_PHP = new rss_php;
        
        $strURL = 'http://emergency.washington.edu/?feed=rss2&cat='.$intCategory;
        $RSS_PHP->load($strURL);

        // Array will always load newest to oldest
        return $RSS_PHP->getItems();
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
?>