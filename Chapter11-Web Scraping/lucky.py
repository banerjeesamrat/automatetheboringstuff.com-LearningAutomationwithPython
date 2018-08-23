#! /usr/bin/python3.5

"""

Author: Samrat Banerjee
Dated: 17/08/2018
Description: Project: “I’m Feeling Lucky” Google Search- Opens several Google search results

"""

import requests,sys,webbrowser,bs4

print('Googling...')    # display text while downloading the Google page
res=requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup=bs4.BeautifulSoup(res.text,"lxml")

# Open a browser tab for each result
linkElems=soup.select('.r a')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
