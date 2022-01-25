from crawl_from_digikala import *

# url = "https://www.digikala.com/search/category-women-shirts/?pageno=1&sortby=4"
# url = "https://www.digikala.com/search/category-notebook-netbook-ultrabook/?pageno=1&sortby=4"
# url = "https://www.digikala.com/search/category-mobile-phone/?pageno=1&sortby=4"
page_url = ["https://www.digikala.com/search/category-book/?pageno=1&sortby=4","https://www.digikala.com/search/category-stationery/?pageno=1&sortby=4",
            "https://www.digikala.com/search/category-musicalinstruments/?pageno=1&sortby=4", "https://www.digikala.com/search/category-handicraft/?pageno=1&sortby=4"]
page_numbers = [277,277, 277,277]
csv_files = ['category-book.csv','category-stationery.csv', "category-musicalinstruments",'category-handicraft']
total_images = []
total_urls = []
total_pages = 4
for j in range(total_pages):
    for i in range(1,page_numbers[j]):
        url = page_url[j]
        print(url.replace(url[url.index("1")], str(i)))
        total_urls = total_urls +  get_url_digikala(url.replace(url[url.index("1")], str(i)))
        total_images = total_images +  get_image_digikala(url.replace(url[url.index("1")], str(i)))
    dict = {'urls': total_urls , 'images' : total_images}
    print(dict)
    df = pd.DataFrame(dict)
    df.to_csv(csv_files[j], index=False)