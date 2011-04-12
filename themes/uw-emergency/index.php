	<?php get_header(); ?>
<body>


 <div id="wheader" class="colorPurple wYes patchNo">
 <div id="autoMargin" style="width: 830px;">
  <div class="wlogoSmall">
   <div class="logoAbsolute"><a id="wlogoLink" href="http://www.washington.edu/">W</a></div>
   <div><a href="http://www.washington.edu/">University of Washington</a></div>
  </div>
  <div id="wsearch">
   <form name="uwglobalsearch" id="searchbox_001967960132951597331:04hcho0_drk" action="http://www.google.com/cse">
    <div class="wfield">
     <input type="hidden" name="cx" value="001967960132951597331:04hcho0_drk" />
     <input type="hidden" name="cof" value="FORID:0" />
     <input name="q" type="text" value="Search the UW" class="wTextInput" onclick="make_blank();" />
    </div>
    <input type="submit" class="formbutton" name="sa" value="Go" />
   </form>
  </div>
  <div id="wtext">
   <ul>
    <li><a href="http://www.washington.edu/">UW Home</a></li>
    <li><span class="wborder"><a href="http://www.washington.edu/home/directories.html">Directories</a></span></li>
    <li><span class="wborder"><a href="http://www.washington.edu/discover/visit/uw-events">Calendar</a></span></li>
    <li><span class="wborder"><a href="http://www.lib.washington.edu/">Libraries</a></span></li>
    <li><span class="wborder"><a href="http://www.washington.edu/maps/">Maps</a></span></li>
    <li><span class="wborder"><a href="http://myuw.washington.edu/">My UW</a></span></li>
   </ul>
  </div>
 </div>
</div> 

	<div id="header">

		<div id="hmenu"> 
		<?php require(TEMPLATEPATH . '/navlinks.php'); ?>
		</div>
		
         
        

	</div>
		
        

	<div class="main">
		<div id="articles">
			<div id="content">
             <div class="headliner style2"><a href="<?php bloginfo('url'); ?>">UW Alert Site</a></div>

            
            <div class="tagline">
            <h3 title="<?php bloginfo('description'); ?>"><?php bloginfo('description'); ?></h2>
            </div>
            
            <div class="uwalert_signup"><a href="http://www.washington.edu/alert/index.php" target="blank">Sign up now for <strong>UW Alert</strong> e-mails and text messages</a> </div>
            
            <br />
            <br />
<br />
			<?php if ($posts) : foreach ($posts as $post) : start_wp(); ?>	  
	         <h2 id="post-<?php the_ID(); ?>"><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php the_title(); ?>"><?php the_title(); ?></a></h2>
		
                <div class="timestamp"><span class="time">Posted at <?php the_time('g:i a') ?> on <?php the_time('l, F j, Y') ?></span></div>
                <div class="timestamp"><span class="time">Last Updated at <?php the_modified_time('g:i a') ?> on <?php the_modified_time('l, F j, Y') ?></span></div>
        
			<?php the_content(__('(more...)')); ?>
		         
            
<div class="date"><span class="entrymeta">
 <?php //_e("Filed under:"); ?> <?php //the_category(',') ?> | <?php edit_post_link('Edit'); ?>
 </span>   <?php wp_link_pages(); ?>
<?php comments_popup_link(__('Comments (0)'), __('Comments (1)'), __('Comments (%)')); ?> </div>  

<br />   

	<!--
	<?php trackback_rdf(); ?>
	-->
	
<?php comments_template(); ?>

<?php endforeach; else: ?>

<p><?php _e('Sorry, no posts matched your criteria.'); ?></p>
<?php endif; ?>
					
<div style="text-align:left;">
<?php posts_nav_link(' | ', 'Next alerts &raquo;', '&laquo; Previous alerts'); ?>
</div>				
				
			</div>
			
			<?php get_sidebar(); ?>	
		<!-- <div id="links">
			<p></p>		
		</div> -->
	</div>	</div>



<?php get_footer(); ?>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-6730222-1");
pageTracker._trackPageview();
} catch(err) {}</script>

</body>	
</html>
