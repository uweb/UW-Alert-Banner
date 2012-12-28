<?php 
header("Cache-Control: no-cache, must-revalidate"); // HTTP/1.1
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT"); // Date in the past

// We want to deliver a overkill static text file
header( 'Content-Type: plain/text, charset=utf-8' );

$strURL = 'http://www.washington.edu/static/UW-Alert-Banner/alert/?test=true';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $strURL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
// TODO Watch timeout and adjust as needed
curl_setopt($ch, CURLOPT_TIMEOUT, 15);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
$strData = curl_exec($ch);
curl_close($ch);

$strDataDecoded = json_decode($strData);

printf("%s\n<break />\n%s", strip_tags($strDataDecoded->{'posts'}[0]->{'title'}), strip_tags($strDataDecoded->{'posts'}[0]->{'excerpt'}));
?>
