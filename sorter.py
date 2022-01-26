from pandas import read_csv
import pandas as pd
df = read_csv("CSV-Files/category_notebook_netbook_ultrabook.csv")
counter = 0
images = df['images']
urls = df['urls']
iamge_path = []
for url in urls:
    counter += 1
    result = df.loc[df['urls'] == url, 'images'].values[0]
    folder_name = './Photos/notbook_ultabook/' + url.split("/")[-1] + '/'
    path_dst_result = folder_name + result.split("/")[-3] + str(counter) + '.jpg'
    iamge_path.append(path_dst_result)
dict = {'urls' : urls,'images': images, 'path': iamge_path}
df = pd.DataFrame(dict)
df.to_csv('CSV-Files/category_notebook_netbook_ultrabook.csv', index=False)
