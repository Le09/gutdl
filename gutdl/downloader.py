import requests
import os
from bs4 import BeautifulSoup


FORMATS = ["epub", "kindle"]
FILE_FORMATS = {"kindle": "mobi"}
ROOT = "https://www.gutenberg.org"


def link_from_number(book_number):
    return "%s/ebooks/%s" % (ROOT, book_number)


def file_format(format):
    return FILE_FORMATS.get(format, format)


def get_title(page_soup):
    return page_soup.h1.text.replace(" by ", " - ")


def has_images(page_soup, link):
    return bool(page_soup.find(about=link + ".epub.images"))


def download_page(book_number):
    link = link_from_number(book_number)
    resp = requests.get(url=link)
    return BeautifulSoup(resp.content, 'html.parser')


def get_title_from_number(book_number):
    page_soup = download_page(book_number)
    return get_title(page_soup)


def download_book(folder_path, book_number):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    os.chdir(folder_path)

    link = link_from_number(book_number)
    page_soup = download_page(book_number)

    title = get_title(page_soup)

    images = "images" if has_images(page_soup, link) else "noimages"
    for format in FORMATS:
        about = "%s.%s.%s" % (link, format, images)
        file_name = "%s.%s" % (title, file_format(format))
        x = page_soup.find(about=about)
        url = ROOT + x.a.get("href")
        resp = requests.get(url=url)
        open(file_name, 'wb').write(resp.content)
