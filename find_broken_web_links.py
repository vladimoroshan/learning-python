#! python3

""" The program goes to the main page and downloads it,
    then searches for an every link, and trying to download all of them. 
    Not working links are resulting output.
    
    url - ('str') http address of testing page
"""

import requests
import bs4 # BeautifulSoup
from os.path import basename

def dead_links(url):
	r = requests.get(url)
	r.raise_for_status() 

	soup = bs4.BeautifulSoup(r.text, 'lxml')
	links = soup.select('a[href]') 
	links_all = []

	for link in links:
		links_all.append(link.get('href'))

	unic_links = set(links_all)
	broken_links = []

	for link in unic_links:
		print('Processing... This may take some time. Thanks for your patience!')
		if not link.startswith('http'): # If relative path
			link = url + link # Make link absolute			

		r = requests.get(link)
		if r.status_code == 404: # Or you can use != 200. Means dead link. Page not found
			broken_links.append(link)

	print('On this site {} broken links.'.format(len(broken_links))) 
	print('Total number of links {}.'.format(len(unic_links))) 
	for broken_link in broken_links:
		print('Non-working link: ', broken_link)

if __name__ == "__main__":
	dead_links('https://automatetheboringstuff.com')
