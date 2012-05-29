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
 *  <script type="text/javascript" src="//emergency.washington.edu/alert.js"></script>
 *  </body>
 *  </html>
 *
 *  Full docs at:
 *  uw.edu/externalaffairs/uwmarketing/toolkits/uw-alert-banner/
 *
 *--------------------------------------------------------------------------*/

$(document).ready(function() {
  $.getJSON('alert.json', function(data) {

    // Alert colors
    types = {
      'red-alert'     : 'red',
      'orange-alert'  : 'orange',
      'blue-alert'    : 'blue',
      'steel-alert'   : 'steel',
      'campus-info'   : 'red',
    };
 
    $.each(data.posts[0].categories, function(key,val) {
      if (types[val.slug]) {
        // Fire up alert
        var strAlertTitle = data.posts[0].title;
        var strAlertLink = '//emergency.washington.edu/';
        var strAlertMessage = data.posts[0].excerpt;
        var strAlertColor = types[val.slug];

        $('body')
          .css({
            'margin'   : '0px',
            'padding'  : '0px'
          })
          .prepend($('<div></div>').attr('id','alertMessage')
            .append(
              $('<div></div>')
                .attr({
                  'id'     : 'alertBox',
                  'class'  : strAlertColor
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