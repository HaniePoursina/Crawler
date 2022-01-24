from crawl_from_digikala import *

# url = "https://www.digikala.com/search/category-women-shirts/?pageno=1&sortby=4"
url = "https://www.digikala.com/search/category-notebook-netbook-ultrabook/?pageno=1&sortby=4"
total_images = []
total_urls = []
page = 240
for i in range(1,page):
    print(url.replace(url[url.index("1")], str(i)))
    total_urls = total_urls +  get_url_digikala(url.replace(url[url.index("1")], str(i)))
    total_images = total_images +  get_image_digikala(url.replace(url[url.index("1")], str(i)))
dict = {'urls': total_urls , 'images' : total_images}
print(dict)
df = pd.DataFrame(dict)
df.to_csv('category_notebook_netbook_ultrabook.csv', index=False)