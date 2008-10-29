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
    
    /**
          * HTML goes here
          */
    $strContent .= '<a href="' . $strLink . '" title ="'. $strTitle .'">More Info</a> &gt;&gt;';

    $strFinal = $_SESSION['hide'] ? '' : "<div id=\"alertBox\"><div id=\"alertBoxText\">" .
    "<h1>Campus Alert:</h1><p>" . $strContent . 
    "</p></div><a href=\"#\" onclick=\"javascript:hideit('alertBox')\">" .
    "<img src=\"close.gif\" name=\"xmark\" width=\"10\" height=\"10\" id=\"xmark\" /></a>" . 
    "<div id=\"clearer\"></div></div>";
    
    echo $strFinal;
?>

