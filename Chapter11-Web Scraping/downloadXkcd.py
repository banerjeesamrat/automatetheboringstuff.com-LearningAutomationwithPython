#! /usr/bin/python3.5

"""

Author: Samrat Banerjee
Dated: 23/08/2018
Description: Project: Downloads every single XKCD comic

"""

import requests,os,bs4

url='https://xkcd.com'              # starting url
os.makedirs('xkcd')   # store comics in ./xkcd
while not url.endswith('#'):
    # Downloading the page
    print('Downloading page %s...'%url)
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text)

    # Find the url of the comic image
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('Could not find comic image.')
    else:
        try:
            comicURL='https:' + comicElem[0].get('src')
            # Download the image
            print("Downloading image %s..."%(comicURL))
            res=requests.get(comicURL)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink=soup.select('a[rel="prev"]')[0]
            url='https://xkcd.com' + prevLink.get('href')
            continue
        # Save the image to ./xkcd
        imageFile=open(os.path.join('xkcd',os.path.basename(comicURL)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # Get the previous button's URL
        prevLink=soup.select('a[rel="prev"]')[0]
        url='https://xkcd.com' + prevLink.get('href')
    print('Done.')
