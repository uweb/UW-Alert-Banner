<?php

$strUrl = 'https://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish';

$objCH = curl_init($strUrl);
curl_setopt($objCH, CURLOPT_HEADER, false);
curl_setopt($objCH, CURLOPT_SSL_VERIFYPEER, false);
curl_exec($objCH);
curl_close($objCH);

?>
