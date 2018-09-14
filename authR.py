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


def write_auth_venue(s,f):        #(s,f):
	try:
		response = urllib2.urlopen(generate_url(s.id))	
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		bib = soup.find_all(id = "gsc_a_b")[0].find_all(class_ = 'gsc_a_tr')
		#print bib
		for bib in bib:
			#title = bib.find("a",class_ = "gsc_a_at").text
			venue = bib.find_all("div", class_ = "gs_gray")[1].text
			#print venue
			f.write('  ' + venue + '\n')
	except:
		return None


#print search('Asif Ekbal')
# s = search('Asif Ekbal')
# print s
# write_auth_venue(s)
# print(interests(s))
