===============
UW Alert Banner
===============

Script used to pull content from emergency (Wordpress) and publish as an alert
banner

Introduction
============

There was a requirement to have an alert banner on the top of pages to signify
an alert. The alert page was done in wordpress and hosted on an external server
so tying into it was a priority. This system takes an json feed and creates a 
banner on the fly via js to pull into a page.

Usage
=====

Following is information on how to activate the UW Alert Banner on your website.
Please note, this is not the same as the UW Alert System. The Alert System is
responsible for SMS, e-mail, phone and other push-stye notification options.
While certain emergencies will require activation of both the UW Alert System
and the Banner, they are separate entities.

When active, the banner displays a brief "alert" on any page where you've pasted
the code (see the installation section below). The banner links to our
emergency blog, which contains more details about the emergency or event that
triggered the alert. The blog also has links and resources that could be useful
during non-emergency situations.

Color Description
=================

The banner is designed to display four different colors, depending on the type
of alert. Here are the general guidelines for when a certain color will be used.
The content of the alert will always provide a much better sense of the actual
emergency than the color will. Also, because events and emergencies are often in
gray areas, similar alerts may be classified differently.


* RED - High level emergency or threat
* ORANGE - Medium emergency or threat
* STEEL - Weather-related notices, FYIs or minor issues

Installation
============

The banner will only show up on the page where you have put the code. If you
want the banner to show on every page, then you’ll want to have your header and
footer in an include or delivered via a content management system. The script is
very lightweight and only contains a few lines of javascript.

Right above the </body> tag::

 <script type="text/javascript" src="//washington.edu/static/alert.js"></script>

That's it!

Testing
-------

To verify the banner will not disrupt any elements on the page, the test code is
available below. The banner will display a steel color and a brief message.

Right above the </body> tag::

 <script type="text/javascript" src="//washington.edu/static/alert-test.js"></script>

