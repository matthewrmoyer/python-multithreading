from bs4 import BeautifulSoup
import urllib.request
import os
import threading


def make_comic_dir():
    os.makedirs('multi-thread-comics', exist_ok=True)


def comic_downloader(starting_comic, ending_comic):
    for i in range(starting_comic, ending_comic):
        url = 'https://xkcd.com/' + str(i)
        print('Downloading from ' + url + '...')
        # open page
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, 'html.parser')
        # find comic url
        comic_divs = soup.select('#comic img')
        if comic_divs == []:
            print('No comic found')
        else:
            comic_url = 'https:' + comic_divs[0].get('src')
            # store comic as div
            target_comic = urllib.request.urlopen(comic_url).read()
            # create comic file name
            en = str(os.path.basename(comic_url))
            img_name = str('_' + en)
            # create comic file
            image_file = open(os.path.join(
                'multi-thread-comics', os.path.basename(url + img_name)), 'wb')
            # write to comic file
            image_file.write(target_comic)
            # close file
            image_file.close()


# make_comic_dir()

# comic_downloader(1, 3)

# multithread!
thread_list = []
for i in range(0, 300, 100):
    # create comic directory
    make_comic_dir()
    # create a thread for every 100 comics
    comic_download_thread = threading.Thread(
        target=comic_downloader, args=[i, i + 99])
    # add the thread to the thread list to keep track of them / when they end
    thread_list.append(comic_download_thread)
    comic_download_thread.start()

# thread.join means the thread is done
for thread in thread_list:
    thread.join()

print('Done')
