/*  University of Washington - Alert 2.0 Beta
 *  (c) 2011 Chris Heiland
 *
 *  Script should be included like such:
 * 
 *  <html>
 *  <head>
 *  <title>Page Title</title>
 *  </head>
 *  <body>
 * 
 *  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
 *  <script type="text/javascript" src="//washington.edu/static/alert.js"></script>
 *  </body>
 *  </html>
 *
 *  Full docs at:
 *  uw.edu/externalaffairs/uwmarketing/toolkits/uw-alert-banner/
 *
 *--------------------------------------------------------------------------*/

var jQueryScriptOutputted = false;
function initJQuery() {
    
  //if the jQuery object isn't available
  if (typeof(jQuery) == 'undefined') {
    if (! jQueryScriptOutputted) {
      //only output the script once..
      jQueryScriptOutputted = true;
      
      //output the script (load it from google api)
      document.write("<scr" + "ipt type=\"text/javascript\" src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js\"></scr" + "ipt>");
    }
    setTimeout("initJQuery()", 50);
  } else {
    jQuery(function($) {
      $.getJSON('alert.php', function(data) {
    
        // Alert colors
        types = {
          'red-alert-urgent' : 'red',
          'orange-alert'     : 'orange',
          'steel-alert-fyis' : 'steel',
          'test'             : 'steel'
        };

        // Because we don't always have alerts
        if (data.posts.length == 0) {
          return false;
        }
     
        $.each(data.posts[0].categories, function(strName,objCategory) {
          if (types[objCategory.slug]) {
            // Fire up alert
            var strAlertTitle = data.posts[0].title;
            var strAlertLink = '//emergency.washington.edu/';
            var strAlertMessage = data.posts[0].excerpt;
            var strAlertColor = types[objCategory.slug];
    
            $('body')
              .css({
                'margin'  : '0px',
                'padding' : '0px'
              })
              .prepend($('<div></div>').attr('id','alertMessage')
                .append(
                  $('<div></div>')
                    .attr({
                      'id'    : 'alertBox',
                      'class' : strAlertColor
                    })
                  .append(
                    $('<div></div>')
                    .attr('id','alertBoxText')
                    .html(
                      $(strAlertMessage)
                        .append(' ') // Needed Spacing
                        .append($('<a></a>')
                          .attr({
                              'href'  : strAlertLink,
                              'title' : strAlertTitle
                          })
                          .text('More Info >>')
                        )
                    )
                    .prepend($('<h1></h1>').html('Campus Alert: '))
                  )
                  .append($('<div></div>').attr('id','clearer'))
                )
              );
          }
        });
      });
    
      // Add some custom styles for the banner
      $('head').append($('<link>')
        .attr({ 
          'href' : '//www.washington.edu/static/uwalert.css',
          'rel'  : 'stylesheet',
          'type' : 'text/css'
        })
      );
    
    });
  }
}

initJQuery();
