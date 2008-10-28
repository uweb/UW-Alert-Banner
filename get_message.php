<?php

	/**
	 * Go get our alert content via an RSS feed out of the emergency blog
	 */    
    session_start();
    if ($_GET['hide'])
    {
        $_SESSION['hide'] = "yes"; 
    }

    include_once('rss_php.php');
    $RSS_PHP = new rss_php; 
    $RSS_PHP->load('http://emergency.washington.edu/?feed=rss2&cat=4');

    $arrItems = $RSS_PHP->getItems();
    
    $strTitle = $arrItems[0]['title'];
    $strLink = $arrItems[0]['link'];
    $strDesc = $arrItems[0]['description'];
    
    // Content length unknown, trim to reasonable length
    $strContent = $strDesc." ";
    $strContent = substr($strContent,0,250);
    $strContent = substr($strContent,0,strrpos($strContent,' '));
    $strContent = $strContent."...";
    
    $strContent .= '<a href="' . $strLink . '" title ="'. $strTitle .'">More Info</a> &gt;&gt;';
    
    $strFinal = $_SESSION['hide'] ? '' : $strContent;
    
    echo $strFinal;
    
    /**
         * HTML goes here
         */  
?>