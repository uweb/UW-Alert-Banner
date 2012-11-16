<?php 
// We want to deliver a dynamic javascript file
header( 'Content-Type: application/javascript' ); 

function get_alert()
{
    $strURL = 'http://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish';
    if ((isset($_GET['test'])) && ($_GET['test'] == 'true'))
        $strURL = 'http://public-api.wordpress.com/rest/v1/sites/en.blog.wordpress.com/posts/?number=1&type=post&status=publish';

    // one of these will work depending on the environment
    $strServerTmp = isset($_SERVER['SERVER_TMPDIR']) ? $_SERVER['SERVER_TMPDIR'].'/uw-alert-banner/' : '/tmp/uw-alert-banner/';

    // We have a good possibility the directory won't be there initially
    if (!is_dir($strServerTmp))
        mkdir($strServerTmp, 0755, true);

    $strCache = $strServerTmp . 'alert.json';
    if ((isset($_GET['test'])) && ($_GET['test'] == 'true'))
        $strCache = $strServerTmp . 'alert-test.json';

    if (file_exists($strCache))
    {
        // How old is the cached data?
        $strTimestamp = filemtime($strCache);
        $objDate = new DateTime();
        $objDate->setTimestamp($strTimestamp);
        $strInterval = $objDate->diff(new DateTime('now'));
        $strCacheAge = $strInterval->format('%i minute(s), %s second(s) old');
    }

    // if the file modification time is less than 30 seconds ago
    if (!file_exists($strCache) || (filemtime($strCache) < (time() - 30)))
    {
        // Get fresh data, it's too old or doesn't exist
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $strURL);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        // TODO Watch timeout and adjust as needed
        curl_setopt($ch, CURLOPT_TIMEOUT, 15);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        // Unnecesary but also doesn't hurt to have
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        $strCacheData = curl_exec($ch);
        curl_close($ch);
        // Dump out actual cached data
        $strCacheFileData = fopen($strCache, 'wb');
        fwrite($strCacheFileData, $strCacheData);
        fclose($strCacheFileData);
        $strCacheState = 'fresh';
    }
    else
    {
        // It's been less than 30 seconds, just used the cache
        $strCacheState = 'stale';
        $strCacheData = file_get_contents($strCache);
    }

    // Adding our own data
    $strCachedDataDecoded = json_decode($strCacheData);
    $strCachedDataDecoded->{'cache_state'} = $strCacheState;
    $strCachedDataDecoded->{'cache_age'} = isset($strCacheAge) ? $strCacheAge : '0';
    $strCacheData = json_encode($strCachedDataDecoded);

    return $strCacheData;
}

$strCallback = isset($_GET['c']) ? $_GET['c'] : '';

echo isset($_GET['c']) ? sprintf('%s(%s)',$_GET['c'],get_alert()) : get_alert();
?>
