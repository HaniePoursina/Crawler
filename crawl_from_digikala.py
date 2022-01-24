from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

def get_url_digikala(page_url):
    htmldata = urlopen(page_url)
    product_title = []
    soup = BeautifulSoup(htmldata, 'html.parser')
    url_sub_str = '"product_url":"'
    mydivs = soup.find_all("a", class_="c-product-box__img c-promotion-box__image js-url js-product-item js-product-url")
    for div in mydivs:
        snt_params = div['data-snt-params']
        if url_sub_str in snt_params:
            url_not_filtered = snt_params.split(url_sub_str, 1)[1]
            size = len(url_not_filtered)
            # Slice string to remove last 3 characters from string
            not_full_url = url_not_filtered[:size - 2]
            product_url = "www.digikala.com" + not_full_url
            product_title.append(product_url)
    return product_title

def get_image_digikala(page_url):
    htmldata = urlopen(page_url)
    product_images = []
    soup = BeautifulSoup(htmldata, 'html.parser')
    mydivs = soup.find_all("a", class_="c-product-box__img c-promotion-box__image js-url js-product-item js-product-url")
    for div in mydivs:
        product_images.append(div.find('img').attrs['src'])
    return product_images

