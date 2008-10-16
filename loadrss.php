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
?>