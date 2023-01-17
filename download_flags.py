import requests
from bs4 import BeautifulSoup
import urllib.request
# from bing_image_downloader import downloader
import os


def flag_downloader(save_dir: str = './flags') -> None:
    """Function for web scraping of countries flag images

    :param save_dir: The folder where the flag images are saved
    """
    URL = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"
    page = requests.get(URL)
    html_soup_object = BeautifulSoup(page.text, 'html.parser')
    # Finding all the flags uisng image class
    image_class = html_soup_object.find_all(class_="image")

    # looping through list of "a" tags, extracting images path and downloading images
    for a in image_class:
        img = a.find('img')
        flag_name = a['title']
        link_url = img["srcset"]
        link_url = link_url.split()[2]  # srcset contains few src
        link_url = 'https:' + link_url
        path = f'{save_dir}/{flag_name}'
        os.makedirs(path, exist_ok=True)
        urllib.request.urlretrieve(
            link_url, f'{save_dir}/{flag_name}/{flag_name}.png')


if __name__ == '__main__':
    flag_downloader()
