<?php
// // /**
// // *loadrss.php - UW Emergency RSS loader
// // *
// // * @name       - loadrss.php
// // * @author     - Chris Heiland <cheiland@u.washington.edu>
// // *
// // * @package    - 
// // * @subpackage - 
// // */
    $ch = curl_init("http://emergency.washington.edu/?feed=rss2&cat=4");
    $fp = fopen("emergency.rss", "w");

    curl_setopt($ch, CURLOPT_FILE, $fp);
    curl_setopt($ch, CURLOPT_HEADER, 0);

    curl_exec($ch);
    curl_close($ch);
    fclose($fp);
    
    //<script type="text/javascript">addToStart()</script>
    include_once('rss_php.php');
    $RSS_PHP = new rss_php; 
    $RSS_PHP->load('emergency.rss');

    $arrItems = $RSS_PHP->getItems();
    
    //var_dump($arrItems);
    $strTitle = $arrItems[0]['title'];
    $strLink = $arrItems[0]['link'];
    $strDesc = $arrItems[0]['description'];
?>