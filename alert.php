<?php 
// We want to deliver a dynamic javascript file
header( 'Content-Type: application/javascript' ); 

// Need to have a test option to along with caching
?>


function doSomething(callback) 
{
    if (callback && typeof(callback) === "function") 
    {
        // execute the callback, passing parameters as necessary
        console.log('executing something');
        var data = {"found":1,"posts":[{"ID":866,"author":{"ID":31416699,"email":false,"name":"uwemergency","URL":"http://uwemergency.wordpress.com","avatar_URL":"http://0.gravatar.com/avatar/62a200f5d7bc7656c7e9f342e13e5547?s=96&d=identicon&r=G","profile_URL":"http://en.gravatar.com/uwemergency"},"date":"2012-08-20T20:06:22+00:00","modified":"2012-08-23T19:04:57+00:00","title":"TEST of Emergency Banner","URL":"http://emergency.uw.edu/2012/08/20/test-of-emergency-banner/","short_URL":"http://wp.me/p2aqbX-dY","content":"<p>This is a test of the UW Alert Banner, there is no emergency, this is only a test.</p>\n","excerpt":"<p>This is a test of the UW Alert Banner, there is no emergency, this is only a test.</p>\n","status":"publish","password":"","parent":false,"type":"post","comments_open":true,"pings_open":true,"comment_count":0,"like_count":0,"format":"standard","geo":false,"publicize_URLs":[],"tags":{},"categories":{"All Locations":{"name":"All Locations","slug":"all-locations","description":"","post_count":1,"parent":6418,"meta":{"links":{"self":"https://public-api.wordpress.com/rest/v1/sites/32036637/categories/slug:all-locations","help":"https://public-api.wordpress.com/rest/v1/sites/32036637/categories/slug:all-locations/help","site":"https://public-api.wordpress.com/rest/v1/sites/32036637"}}},"Steel Alert (FYIs)":{"name":"Steel Alert (FYIs)","slug":"steel-alert-fyis","description":"Ideal for info posted between alerts like campus weather closures.","post_count":1,"parent":6418,"meta":{"links":{"self":"https://public-api.wordpress.com/rest/v1/sites/32036637/categories/slug:steel-alert-fyis","help":"https://public-api.wordpress.com/rest/v1/sites/32036637/categories/slug:steel-alert-fyis/help","site":"https://public-api.wordpress.com/rest/v1/sites/32036637"}}},"Safe Campus":{"name":"Safe Campus","slug":"safe-campus","description":"","post_count":1,"parent":0,"meta":{"links":{"self":"https://public-api.wordpress.com/rest/v1/sites/32036637/categories/slug:safe-campus","help":"https://public-api.wordpress.com/rest/v1/sites/32036637/categories/slug:safe-campus/help","site":"https://public-api.wordpress.com/rest/v1/sites/32036637"}}}},"attachments":{},"meta":{"links":{"self":"https://public-api.wordpress.com/rest/v1/sites/32036637/posts/866","help":"https://public-api.wordpress.com/rest/v1/sites/32036637/posts/866/help","site":"https://public-api.wordpress.com/rest/v1/sites/32036637","replies":"https://public-api.wordpress.com/rest/v1/sites/32036637/posts/866/replies/","likes":"https://public-api.wordpress.com/rest/v1/sites/32036637/posts/866/likes/"}}}]};
        callback(data);
    }
}

doSomething(<?php echo $_GET['c']; ?>);



