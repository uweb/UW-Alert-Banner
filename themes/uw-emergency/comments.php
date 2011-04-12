<!-- Theme by Sreejith R - http://www.GFXedit.com / http://www.sr-ultimate.com  -->


<?php if ( !empty($post->post_password) && $_COOKIE['wp-postpass_' . COOKIEHASH] != $post->post_password) : ?>
<p><?php _e('Enter your password to view comments.'); ?></p>
<?php return; endif; ?>

<h4 id="comments"><?php comments_number(__('No Comments'), __('1 Comment'), __('% Comments')); ?> 
<?php if ( comments_open() ) : ?>
	<a href="#postcomment" title="<?php _e("Leave a comment"); ?>"><strong>&raquo;</strong></a>
<?php endif; ?>
</h4>


<?php if ( $comments ) : ?>
<ol id="commentlist">

<?php foreach ($comments as $comment) : ?>
	<li id="comment-<?php comment_ID() ?>">
	<?php comment_text() ?>
	<p><cite><?php comment_type(__('Comment'), __('Trackback'), __('Pingback')); ?> <?php _e('by'); ?> <?php comment_author_link() ?> &#8212; <?php comment_date() ?> @ <a href="#comment-<?php comment_ID() ?>"><?php comment_time() ?></a></cite> <?php edit_comment_link(__("Edit This"), ' |'); ?></p>
	</li>

<?php endforeach; ?>

</ol>

<?php else : // If there are no comments yet ?>
	<p><?php _e('No comments yet.'); ?></p>
<?php endif; ?>

<!--  HERE you can add links to different feeds and utility sites like digg -->
<p><?php comments_rss_link(__('<abbr title="Really Simple Syndication">RSS</abbr> feed for comments on this post.')); ?> 
<?php if ( pings_open() ) : ?>
	 | <a href="<?php trackback_url() ?>" rel="trackback"><?php _e('TrackBack <abbr title="Uniform Resource Identifier">URI</abbr>'); ?></a> <br />
  You can also <a href="http://del.icio.us/post?url=<?php the_permalink() ?>&amp;title=<?php the_title(); ?>" title="Bookmark this entry on del.icio.us"><abbr title="Bookmark this on del.icio.us">bookmark 
  this</abbr></a> on del.icio.us or check the <a href="http://technorati.com/cosmos/search.html?url=<?php the_permalink() ?>"><abbr title="See this page in technorati">cosmos</abbr></a> 
  <!--  end -->
  <?php endif; ?>
</p>

<?php if ( comments_open() ) : ?>
<h4 id="postcomment"><?php _e('Leave a comment'); ?></h4>

<?php if ( get_option('comment_registration') && !$user_ID ) : ?>
<p>You must be <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?redirect_to=<?php the_permalink(); ?>">logged in</a> to post a comment.</p>
<?php else : ?>

<form action="<?php echo get_option('siteurl'); ?>/wp-comments-post.php" method="post" id="commentform">

<?php if ( $user_ID ) : ?>

<p>Logged in as <a href="<?php echo get_option('siteurl'); ?>/wp-admin/profile.php"><?php echo $user_identity; ?></a>. <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?action=logout" title="<?php _e('Log out of this account') ?>">Logout &raquo;</a></p>

<?php else : ?>

<p><input type="text" name="author" id="author" value="<?php echo $comment_author; ?>" size="22" tabindex="1" />
<label for="author"><small>Name <?php if ($req) _e('(required)'); ?></small></label></p>

<p><input type="text" name="email" id="email" value="<?php echo $comment_author_email; ?>" size="22" tabindex="2" />
<label for="email"><small>Mail (will not be published) <?php if ($req) _e('(but required)'); ?></small></label></p>

<p><input type="text" name="url" id="url" value="<?php echo $comment_author_url; ?>" size="22" tabindex="3" />
<label for="url"><small>Website</small></label></p>

<?php endif; ?>

<p><small><strong>XHTML</strong> ( You can use these tags): <?php echo allowed_tags(); ?>.</small></p>

<p><textarea name="comment" id="comment" cols="55" rows="11" tabindex="4"></textarea></p>

<p><input name="submit" type="submit" id="submit" tabindex="5" value="<?php _e("Press me now"); ?>" class="search-button" />

<input type="hidden" name="comment_post_ID" value="<?php echo $id; ?>" />
</p>
<?php do_action('comment_form', $post->ID); ?>

</form>

<?php endif; // If registration required and not logged in ?>

<?php else : // Comments are closed ?>
<p><?php _e('Sorry, the comment form is closed at this time.'); ?></p>
<?php endif; ?>
<!-- This is where the "NEXT"  & "PREVIOUS" links appears after comments-->
<div class="pg_nav"><?php previous_post('&laquo; %', '', 'yes'); ?> 
&nbsp;&nbsp; <?php next_post('% &raquo;', '', 'yes'); ?></div>
<!--  end -->


<!-- Theme by Sreejith R - http://www.GFXedit.com / http://www.sr-ultimate.com  -->
