<div id="right">
				
                
				<div class="rightarticle" style="border: #CCCCCC 1px solid">
                
           
   <!-- <?php wp_list_pages(); ?> -->              
                
<?php /* If this is a category archive */ if (is_home()) { ?>  
 <?php
 $link_cats = $wpdb->get_results("SELECT cat_id, cat_name FROM $wpdb->linkcategories");
 foreach ($link_cats as $link_cat) {
 ?>

   <h2><?php echo $link_cat->cat_name; ?></h2>
<ul><?php wp_get_links($link_cat->cat_id); ?> </ul>


 <?php } ?><?php } ?>
 
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
