#This module returns h-index of the authors, document count of the affiliation 
#and citation count of the reference paper

#!/usr/bin/env python
#import gscholar
import requests
import json
import scholarly
import urllib2
from bs4 import BeautifulSoup


def generate_url(idd):
	link = 'https://scholar.google.co.in/citations?user='+idd+'&hl=en'
	return link


def search(name):
	try:
		sarch = next(scholarly.search_author(name))
		return sarch
	except:
		return None
def interests(s):
	return s.interests


def write_auth_venue(s,f,g):
	try:
		response = urllib2.urlopen(generate_url(s.id))	
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		bib = soup.find_all(id = "gsc_a_b")[0].find_all(class_ = 'gsc_a_tr')
		for bib in bib:
			title = bib.find("a",class_ = "gsc_a_at").text
			year = bib.find(class_ = "gsc_a_y").text
			venue = bib.find_all("div", class_ = "gs_gray")[1].text
			#f.write('  ' + venue + '\t' + year + '\n')
			g.write(' ' + title + '\t' + year + '\n')
	except:
		return None


# s = search('Asif Ekbal')
# print s
# print(write_auth_venue(s))
