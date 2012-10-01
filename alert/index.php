<?php 
// We want to deliver a dynamic javascript file
header( 'Content-Type: application/javascript' ); 

// TODO Need to have a test option
function get_alert()
{

    // $url = '//public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish&callback=displayAlert';
    $url = 'http://public-api.wordpress.com/rest/v1/sites/uwemergency.wordpress.com/posts/?number=1&type=post&status=publish';
    // one of these will work TODO need to test it
    $strServerTmp = isset($_SERVER['SERVER_TMPDIR']) ? $_SERVER['SERVER_TMPDIR'].'/uw-alert-banner/' : '/tmp/uw-alert-banner/';

    // We have a good possibility the directory won't be there initially
    if (!is_dir($strServerTmp))
        mkdir($strServerTmp, 0755, true);

    $cache = $strServerTmp . 'alert.json';

    // if the file modification time is less than 30 seconds ago
    if(filemtime($cache) < (time() - 30))
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
?>

function grabAlertData(callback) 
{
    if (callback && typeof(callback) === "function") 
    {
        // execute the callback, passing parameters as necessary
        var data = <?php echo get_alert(); ?>;
        callback(data);
    }
}

grabAlertData(<?php echo $_GET['c']; ?>);
