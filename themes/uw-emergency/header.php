<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title><?php bloginfo('name'); ?><?php wp_title(); ?></title>
<meta http-equiv="Content-Type" content="text/html; charset=<?php bloginfo('charset'); ?>" />
<meta name="generator" content="WordPress <?php bloginfo('version'); ?>" /> <!-- leave this for stats -->
<meta name="description" content="GFXedit.com, Wordpress Themes"/>
<meta name="keywords" content="wordpress, themes, customization, templates, wpthemes, "/>
<meta name="author" content="Sreejith"/>
<style type="text/css" media="screen">
@import url( <?php bloginfo('stylesheet_url'); ?> );
</style>
<meta name="copyright" content="University of Washington" />
<meta name="Author" content="Luka Cvrk (luka@solucija.com)" />
<meta name="wp-theme" content="Sreejith R - GFXedit.com" />
<meta name="generator" content="WordPress <?php bloginfo('version'); ?>" />
<meta name="robots" content="index,follow" />

<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="<?php bloginfo('rss2_url'); ?>" />
<link rel="alternate" type="text/xml" title="RSS .92" href="<?php bloginfo('rss_url'); ?>" />
<link rel="alternate" type="application/atom+xml" title="Atom 0.3" href="<?php bloginfo('atom_url'); ?>" />
<link rel="pingback" href="<?php bloginfo('pingback_url'); ?>" />

<link rel="stylesheet" href="http://depts.washington.edu/uweb/inc/css/header.css" type="text/css" media="screen" />
<link rel="stylesheet" href="http://depts.washington.edu/uweb/inc/css/print.css" type="text/css" media="print" />
<script type="text/javascript">
// clear out the global search input text field
function make_blank() {if(document.uwglobalsearch.q.value=="Search the UW") {document.uwglobalsearch.q.value = "";}}
</script>

<?php wp_get_archives('type=monthly&format=link'); ?>
<?php //comments_popup_script(); // off by default ?>
<?php wp_head(); ?>

</head>