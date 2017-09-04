from bs4 import BeautifulSoup
import urllib.request
import os
import threading


url = 'https://xkcd.com/'


os.getcwd()
os.makedirs('comics', exist_ok=True)

while not url.endswith('#'):
    print('Dowloading from %s...' % url)

    # get the page
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source)

    # find comic in page
    comic = soup.select('#comic img')
    if comic == []:
        print('No comic found')
    else:
        # find url src of comic img
        comic_url = 'https:' + comic[0].get('src')
        print('Downloading image from %s' % comic_url)
        # set variable to comic / the url page of the comic url
        target_comic = urllib.request.urlopen(comic_url).read()
        # create comic file
        image_file = open(os.path.join(
            'comics', os.path.basename(comic_url)), 'wb')
        # write to comic file
        image_file.write(target_comic)
        # close file
        image_file.close

    # get url of previous comic button
    previous_link = soup.select('a[rel="prev"]')[0]
    # set the url variable to the previous comic
    url = 'https://xkcd.com' + previous_link.get('href')


print('Done')
