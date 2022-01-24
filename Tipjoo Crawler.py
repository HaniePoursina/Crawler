import os
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse


def scrapper(url):
    # htmldata = urlopen('http://tipjoo.com/Home/Products/woman')
    # htmldata = urlopen('https://www.digistyle.com/category-women-clothing/')
    htmldata = urlopen(url)

    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    titles = soup.find_all('h5')

    product_title = []
    product_urls = []
    product_substring = "/ASHXs/LoadImage.ashx?fileName=Product"

    for item in images:
        if product_substring in item['src']:
            product_urls.append("http://tipjoo.com" + item['src'])
    print("urls", product_urls)
    #
    for item in titles:
        try:
            for x in item["class"]:
                product_title.append(item.string)
        except:
            continue
    print(product_title)

    for i in range(len(product_urls)):
        urllib.request.urlretrieve(product_urls[i], os.path.join("./Scrapped-Images/", product_title[i]+".jpg"))


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Enter URL of the Website you need to crawl')
#     parser.add_argument('--website', dest='website', type=str, help='The Website You need to crawl')
#
#     args = parser.parse_args()
# scrapper(args.website)

scrapper("http://tipjoo.com/Home/Products/woman")