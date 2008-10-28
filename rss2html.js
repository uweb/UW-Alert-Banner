//OBJECTS

//objects inside the RSS2Item object
function RSS2Enclosure(encElement)
{
	if (encElement == null)
	{
		this.url = null;
		this.length = null;
		this.type = null;
	}
	else
	{
		this.url = encElement.getAttribute("url");
		this.length = encElement.getAttribute("length");
		this.type = encElement.getAttribute("type");
	}
}

function RSS2Guid(guidElement)
{
	if (guidElement == null)
	{
		this.isPermaLink = null;
		this.value = null;
	}
	else
	{
		this.isPermaLink = guidElement.getAttribute("isPermaLink");
		this.value = guidElement.childNodes[0].nodeValue;
	}
}

function RSS2Source(souElement)
{
	if (souElement == null)
	{
		this.url = null;
		this.value = null;
	}
	else
	{
		this.url = souElement.getAttribute("url");
		this.value = souElement.childNodes[0].nodeValue;
	}
}

//object containing the RSS 2.0 item
function RSS2Item(itemxml)
{
	//required
	this.title;
	this.link;
	this.description;

	//optional vars
	this.author;
	this.comments;
	this.pubDate;

	//optional objects
	this.category;
	this.enclosure;
	this.guid;
	this.source;

	var properties = new Array("title", "link", "description", "author", "comments", "pubDate");
	var tmpElement = null;
	for (var i=0; i<properties.length; i++)
	{
		tmpElement = itemxml.getElementsByTagName(properties[i])[0];
		if (tmpElement != null)
			eval("this."+properties[i]+"=tmpElement.childNodes[0].nodeValue");
	}

	this.category = new RSS2Category(itemxml.getElementsByTagName("category")[0]);
	this.enclosure = new RSS2Enclosure(itemxml.getElementsByTagName("enclosure")[0]);
	this.guid = new RSS2Guid(itemxml.getElementsByTagName("guid")[0]);
	this.source = new RSS2Source(itemxml.getElementsByTagName("source")[0]);
}

//objects inside the RSS2Channel object
function RSS2Category(catElement)
{
	if (catElement == null)
	{
		this.domain = null;
		this.value = null;
	}
	else
	{
		this.domain = catElement.getAttribute("domain");
		this.value = catElement.childNodes[0].nodeValue;
	}
}

//object containing RSS image tag info
function RSS2Image(imgElement)
{
	if (imgElement == null)
	{
	this.url = null;
	this.link = null;
	this.width = null;
	this.height = null;
	this.description = null;
	}
	else
	{
		imgAttribs = new Array("url","title","link","width","height","description");
		for (var i=0; i<imgAttribs.length; i++)
			if (imgElement.getAttribute(imgAttribs[i]) != null)
				eval("this."+imgAttribs[i]+"=imgElement.getAttribute("+imgAttribs[i]+")");
	}
}

//object containing the parsed RSS 2.0 channel
function RSS2Channel(rssxml)
{
	//required
	this.title;
	this.link;
	this.description;

	//array of RSS2Item objects
	this.items = new Array();

	//optional vars
	this.language;
	this.copyright;
	this.managingEditor;
	this.webMaster;
	this.pubDate;
	this.lastBuildDate;
	this.generator;
	this.docs;
	this.ttl;
	this.rating;

	//optional objects
	this.category;
	this.image;

	var chanElement = rssxml.getElementsByTagName("channel")[0];
	var itemElements = rssxml.getElementsByTagName("item");

	for (var i=0; i<itemElements.length; i++)
	{
		Item = new RSS2Item(itemElements[i]);
		this.items.push(Item);
		//chanElement.removeChild(itemElements[i]);
	}

	var properties = new Array("title", "link", "description", "language", "copyright", "managingEditor", "webMaster", "pubDate", "lastBuildDate", "generator", "docs", "ttl", "rating");
	var tmpElement = null;
	for (var i=0; i<properties.length; i++)
	{
		tmpElement = chanElement.getElementsByTagName(properties[i])[0];
		if (tmpElement!= null)
			eval("this."+properties[i]+"=tmpElement.childNodes[0].nodeValue");
	}

	this.category = new RSS2Category(chanElement.getElementsByTagName("category")[0]);
	this.image = new RSS2Image(chanElement.getElementsByTagName("image")[0]);
}

//PROCESSES

// //uses xmlhttpreq to get the raw rss xml
function getRSS()
{
	//call the right constructor for the browser being used
	if (window.ActiveXObject)
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	else if (window.XMLHttpRequest)
		xhr = new XMLHttpRequest();
	else
		alert("not supported");

        
	//prepare the xmlhttprequest object
	//xhr.open("GET",document.rssform.rssurl.value,true);
    xhr.open("GET",'emergency.rss',true);
	xhr.setRequestHeader("Cache-Control", "no-cache");
	xhr.setRequestHeader("Pragma", "no-cache");
	xhr.onreadystatechange = function()
    {
		if (xhr.readyState == 4)
		{
			if (xhr.status == 200)
			{
				if (xhr.responseText != null)
					processRSS(xhr.responseXML);
				else
				{
					alert("Failed to receive RSS feed from the emergency server - service not available.");
					return false;
				}
			}
			else
				alert("Error code " + xhr.status + " received: " + xhr.statusText);
		}
	}

	//send the request
	xhr.send(null);
}

//processes the received rss xml
function processRSS(rssxml)
{
	RSS = new RSS2Channel(rssxml);
	showRSS(RSS);
}

//shows the RSS content in the browser
function showRSS(RSS)
{
	//default values for html tags used
    var strHTML = '';
    var startWrapper = '<div id="alertBox">';
	var startItemTag = '  <div id="alertBoxText">';
	var startTitle = '    <h1>Campus Alert:</h1> ';
    var clearTag = '<div id="clearer"></div> ';
    var closeTag = '  <img src="close.gif" name="xmark" width="10" height="10" id="xmark" />';
	var endTag = '</div>';

	//populate the items
	for (var i=0; i<RSS.items.length; i++)
	{
        strHTML = startWrapper;
		strHTML += startItemTag;
        strHTML += startTitle;
		// strHTML += (RSS.items[i].title == null) ? "" : startTitle + RSS.items[i].title + endTag;
		// strHTML += (RSS.items[i].link == null) ? "" : startLink + RSS.items[i].link + endTag;
		strHTML += (RSS.items[i].description == null) ? "" : RSS.items[i].description + endTag;
        strHTML += closeTag;
        strHTML += clearTag;
		strHTML += endTag;
	}

    addtoStart(strHTML);
    
	//we're done
    //document.getElementById("chan").style.visibility = "visible";
	return true;
}

//<script type="text/javascript">addToStart()</script> 
function addToStart(strHTML)
{

	// first we create a new div with document.createElement()
	//var newcontent = document.createElement('div');
    var newcontent = document.write(strHTML);

	// then we create some text with document.createTextNode()
	//var newtext = document.createTextNode(strText);

	// then we put the text in the div
	//newcontent.appendChild(newtext);

	// and you can nest/combine them like this to add more text
	//newcontent.appendChild(document.createTextNode('  It looks like a nice day!'));

	// then we want to get a reference to the body tag with document.getElementsByTagName()
	// this returns an array, so we only take the first result by specifying the [0] at the end
	var bodytag = document.getElementsByTagName('body')[0];

	// now we want to append 'newcontent' to 'bodytag' -- but not at the end
	// to prepend (insert at the beginning) we need to 'insert before' the 'first child' of the body tag
	// we do this by using the DOM's .insertBefore() method and .firstChild property:
	bodytag.insertBefore(newcontent,bodytag.firstChild);

}

var xhr;