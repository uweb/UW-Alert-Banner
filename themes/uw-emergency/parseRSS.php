<?php

// http://www.stemkoski.com/how-to-easily-parse-a-rss-feed-with-php-4-or-php-5/

	function parseRSS($url) { 
 
	//PARSE RSS FEED
        $feedeed = implode('', file($url));
        $parser = xml_parser_create();
        xml_parse_into_struct($parser, $feedeed, $valueals, $index);
        xml_parser_free($parser);
 
	//CONSTRUCT ARRAY
        foreach($valueals as $keyey => $valueal){
            if($valueal['type'] != 'cdata') {
                $item[$keyey] = $valueal;
			}
        }
 
        $i = 0;
 
        foreach($item as $key => $value){
 
            if($value['type'] == 'open') {
 
                $i++;
                $itemame[$i] = $value['tag'];
 
            } elseif($value['type'] == 'close') {
 
                $feed = $values[$i];
                $item = $itemame[$i];
                $i--;
 
                if(count($values[$i])>1){
                    $values[$i][$item][] = $feed;
                } else {
                    $values[$i][$item] = $feed;
                }
 
            } else {
                $values[$i][$value['tag']] = $value['value'];  
            }
        }
 
	//RETURN ARRAY VALUES
        return $values[0];
	} 
	
?>