import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import csv
package_list = []

for i in package_list:
	alist = [i]
	try:
		# page = urllib2.urlopen('https://www.appbrain.com/app/india-news/ticketnew.android.ui' + i)
		opener = urllib2.build_opener()
		opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
		page = opener.open('https://www.appbrain.com/app/india-news/' + i)
		soup = BeautifulSoup(page.read(), 'html.parser')
		for w in soup.findAll("div", { "class" : "infotiles" }):
			alist.append(w.text)
			lst.append(alist)
			print i
	except urllib2.HTTPError, error:
		contents = error.read()
		# print contents

# print lst
