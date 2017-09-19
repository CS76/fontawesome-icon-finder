#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Venkata chandrasekhar Nainala 
# Version: 0.1.0
# Email: mailcs76@gmail.com 

""" Scrape 
"""

import os
import sys
import json
import urllib2
import argparse
import csv
from os.path import basename
from bs4 import BeautifulSoup, NavigableString
from algoliasearch import algoliasearch

icons = []

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    args = parser.parse_args(arguments)
    scrapeFontAwesomeCheatsheet()

def scrapeFontAwesomeCheatsheet():
	client = algoliasearch.Client("**********", "************************")
	index = client.init_index('font_awesome')
	fontawesomeURL = "http://fontawesome.io/icons/";
	cheatSheetHTML = urllib2.urlopen(fontawesomeURL).read();
	cheatSheetSoup = BeautifulSoup(cheatSheetHTML, "html.parser")
	wrapperDiv = cheatSheetSoup.find("div", { "id" : "icons" })
	fonts = wrapperDiv.findAll("div", { "class" : "fa-hover" })
	i = 0
	global icons
	for font in fonts:
		icon = {}
		faIcon = font.findAll("a")[0]['href'].replace("../icon/","")
		aliases = font.findAll("span", { "class" : "text-muted" })
		icon["search"] = []
		if len(aliases) > 0:
			for alias in aliases:
				if len(alias.findAll("em")) > 0:
					icon["search"].append((alias.findAll("em")[0]).text)
		icon["search"].append(faIcon) 
		try:
			fontawesomeIconURL = "http://fontawesome.io/icon/" + faIcon
			fontawesomeIconHTML = urllib2.urlopen(fontawesomeIconURL).read();
			fontawesomeIconSoup = BeautifulSoup(fontawesomeIconHTML, "html.parser")
			icon["name"] = faIcon
			h1Div = fontawesomeIconSoup.findAll("h1", { "class" : "info-class" })[0]
			icon["class"] = ''.join([element for element in h1Div if isinstance(element, NavigableString)]).replace("\n","").strip()
			icon["unicode"] = '&#x' + (h1Div.findAll("span", { "class" : "upper" })[0]).text + ";"
			smallDiv = h1Div.findAll("small")[0]
			smallDivContent = ''.join([element for element in smallDiv if isinstance(element, NavigableString)]).replace("\n","").strip().split(u'·')
			icon["version"] = (smallDivContent[2].split(":")[1]).strip()
			icon["categories"] = (smallDivContent[3].split(":")[1]).strip()
			icon["objectID"] = faIcon
			icons.append(icon)
		except:
			pass
		i = i+1
		print i
	index.add_objects(icons)
	writeDataToFile("data.json",icons)

def writeDataToFile(filename, data):
    with open(filename, "w") as fp:
        json.dump(data, fp)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))