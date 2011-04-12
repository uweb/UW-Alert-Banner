<div id="right">

		<div class="rightarticle" style="border: #CCCCCC 1px solid">
        
    <h2>Quick Contacts</h2>
        <ul class="links">
            <li><a href="http://www.washington.edu/admin/police/">UW Police: 206-685-UWPD (8973)</a></li>
            <li><a href="http://www.uwb.edu/safety/">Bothell: 425-352-5359</a></li>
            <li><a href="http://www.tacoma.washington.edu/security/">Tacoma: 253-692-4416</a></li>
        </ul>
 

<!-- <h2>Photos<img src="
http://www.washington.edu/uwnews/homepage/images/alert_photos.gif" hspace="10" border="0"></h2>
         <ul>
           <li><a href="http://emergency.washington.edu/?page_id=51">View Snowstorm Slideshow</a></li>
        </ul> -->



<h2>Web Cams </h2>

<a href="http://www.atmos.washington.edu/images/webcam0/"><img src="http://www.atmos.washington.edu/images/webcam0/latest.jpg" vspace="10" border="0" style="border: 1px solid #000;" width="200" height="118" alt="Latest rooftop image" /></a>

<br /><a href="http://www.atmos.washington.edu/images/webcam0/">Time-lapse movies | More</a>

<!--<a href="http://www.washington.edu/cambots/"><img src="http://www.washington.edu/home/cambots/camera1.jpg" vspace="10" border="0" style="border: 1px solid #000;" alt="Red square cam image" width="200" height="118" /></a>

<br /><a href="http://www.washington.edu/cambots/">Red Square | More</a>-->

<a href="http://www.seattle.gov/trafficcams/"><img width="200" height="118" vspace="10" border="0" style="border: 1px solid #000;" src="http://www.seattle.gov/trafficcams/images/Montlake_25.jpg
" alt="Montlake traffic cam image" /></a>

<br /><a href="http://www.seattle.gov/trafficcams/">Traffic Cams | More</a><br /><br />

<h2>Current Conditions</h2>
<?php
require_once('parseRSS.php');
$xml = parseRSS("http://www.weather.gov/data/current_obs/KBFI.rss");

//SAMPLE USAGE OF 
foreach($xml['RSS']['CHANNEL']['ITEM'] as $item) 
{
    echo("<p>{$item['TITLE']}{$link}</p>");
}
?>	

  <!-- <?php wp_list_pages(); ?> -->              
                
 <?php
 $link_cats = $wpdb->get_results("SELECT cat_id, cat_name FROM $wpdb->linkcategories");
 foreach ($link_cats as $link_cat) {
 ?>

   <h2><?php echo $link_cat->cat_name; ?></h2>
<ul><?php wp_get_links($link_cat->cat_id); ?> </ul>


 <?php } ?>
 
<!-- <div id="rightmenu">
 					<?php list_cats(0, '', 'name', 'ASC', '/', true, 0, 0);    ?>
 				
 				</div>	<div id="searchform">
 					<form id="searchform" method="get"  class="search" action="<?php echo $PHP_SELF; ?>">	
 							<p>
 							<input type="text" class="text" name="s" id="s" size="15" /><br />
 					<input type="submit" class="button"  name="submit" value="<?php _e('Search'); ?>" />
 </p>
   						</form>
					</div>
				
					
					<p style="border-top: #CCCCCC 1px dashed"></p>
						<h2> <?php _e('Archives:'); ?></h2>
				
				
							<?php wp_get_archives('type=monthly'); ?>		

				 <?php if (function_exists('wp_theme_switcher')) { ?>
 <h2>Styleswitcher</h2> 
<?php wp_theme_switcher(); ?>
<?php } ?> -->


		<?php /* If this is a category archive */ if (is_home()) { ?>  	<ul style="border-top: #CCCCCC 1px dashed">
				<?php wp_register(); ?>
		<li><?php wp_loginout(); ?></li>

		<li><a href="<?php bloginfo('rss2_url'); ?>" title="<?php _e('Syndicate this site using RSS'); ?>"><?php _e('<abbr title="Really Simple Syndication">RSS</abbr>'); ?></a></li>
		<li><a href="<?php bloginfo('comments_rss2_url'); ?>" title="<?php _e('The latest comments to all posts in RSS'); ?>"><?php _e('Comments <abbr title="Really Simple Syndication">RSS</abbr>'); ?></a></li>
		<li><a href="http://validator.w3.org/check/referer" title="<?php _e('This page validates as XHTML 1.0 Transitional'); ?>"><?php _e('Valid <abbr title="eXtensible HyperText Markup Language">XHTML</abbr>'); ?></a></li>
		<li><a href="http://gmpg.org/xfn/" ><abbr title="XHTML Friends Network">XFN</abbr></a></li>
		
        

		<?php wp_meta(); ?>

		</ul>
 <?php } ?>
				</div><p style="border-top: #CCCCCC 1px dashed"></p>
		</div>
		</div>
