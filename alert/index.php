<?php 
// We want to deliver a dynamic javascript file
header( 'Content-Type: application/javascript' ); 

// TODO Need to have a test option
function get_alert()
{
    $url = 'http://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish';
    if ((isset($_GET['test'])) && ($_GET['test'] == 'true'))
        $url = 'http://public-api.wordpress.com/rest/v1/sites/en.blog.wordpress.com/posts/?number=1&type=post&status=publish';

    // $url = '//public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish&callback=displayAlert';
    // one of these will work depending on the environment
    $strServerTmp = isset($_SERVER['SERVER_TMPDIR']) ? $_SERVER['SERVER_TMPDIR'].'/uw-alert-banner/' : '/tmp/uw-alert-banner/';

    // We have a good possibility the directory won't be there initially
    if (!is_dir($strServerTmp))
        mkdir($strServerTmp, 0755, true);

    $cache = $strServerTmp . 'alert.json';
    if ((isset($_GET['test'])) && ($_GET['test'] == 'true'))
        $cache = $strServerTmp . 'alert-test.json';


    // if the file modification time is less than 30 seconds ago
    if (!file_exists($cache) || (filemtime($cache) < (time() - 30)))
    {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
        // TODO Watch timeout and adjust as needed
        curl_setopt($ch, CURLOPT_TIMEOUT, 5);
        // Unnecesary but also doesn't hurt to have
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        $data = curl_exec($ch);
        curl_close($ch);
        // Dump out actual cached data
        $cachefile = fopen($cache, 'wb');
        fwrite($cachefile, $data);
        fclose($cachefile);
    }
    else
    {
        $data = file_get_contents($cache);
    }
    return $data;
}

$strCallback = isset($_GET['c']) ? $_GET['c'] : '';

echo isset($_GET['c']) ? $_GET['c'].'('.get_alert().')' : get_alert();
?>
