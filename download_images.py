import os

import requests
import pandas as pd
import shutil


# def download_images(file_to_download):
#     df = pd.read_csv(path_csv)
#     urls = data['urls'].tolist()
#
#     counter = 0
#
#     save_path = path_to_download
#     for url in urls:
#         filename = url.split("/")[-1] + ".jpg"
#         completeName = os.path.join(save_path, filename)
#         counter += 1
#         img_data = requests.get(image).content
#         with open(completeName, 'wb') as handler:
#             handler.write(img_data)
#         handler.close()
counter = 0
df = pd.read_csv("category_notebook_netbook_ultrabook.csv")
images = df['images']
urls = df['urls']
path = []

for url in urls:
    counter += 1
    image_file = './Photos/notbook_ultabook/' + url.split("/")[-1]
    folder_name = './Photos/notbook_ultabook/' + url.split("/")[-1] + '/'
    result = df.loc[df['urls'] == url, 'images'].values[0]
    path_src_result = './Photos/notbook_ultabook/' + result.split("/")[-3] + ".jpg"
    path_dst_result = folder_name + result.split("/")[-3] + str(counter) + '.jpg'
    path.append(path_dst_result)

    # Check if any folder with name of that url exists
    isExist = os.path.exists(image_file)
    if isExist:

        # Check if the image already downloaded or not
        if os.path.exists(path_src_result):
            shutil.move(path_src_result, folder_name)
            print("moved")

        # Download the image, If image has not been downloaded
        else:
            img_data = requests.get(result).content
            with open(path_dst_result, 'wb') as handler:
                handler.write(img_data)
            handler.close()

    # No folder with that url exists
    if not isExist:
        os.makedirs(image_file)

        # Check if the image already downloaded or not
        if os.path.exists(path_src_result):
            shutil.move(path_src_result,folder_name)
            print("moved")

        # Download the image, If image has not been downloaded
        else:
            img_data = requests.get(result).content
            with open(path_dst_result, 'wb') as handler:
                handler.write(img_data)
            handler.close()
dict = {'urls' : urls,'images': images, 'path': path}
df = pd.DataFrame(dict)
df.to_csv('category_notebook_netbook_ultrabook.csv', index=False)