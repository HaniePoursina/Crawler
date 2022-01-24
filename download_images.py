import os

import requests
import pandas as pd


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
df = pd.read_csv("category_wemon_shirts.csv")
names = [(item.split("/")[-1]) for item in df['urls'].tolist()]
images = [(item.split("/")[-3]) for item in df['images'].tolist()]
for name in names:
    counter += 1
    isExist = os.path.exists('./Photos/Wemon_Shirts/' + name)
    if isExist:
        save_path = './Photos/Wemon_Shirts/' + name
        result = df.loc[df['urls'] == name, 'images'].values[0]
        print(result)
#     file_path = './Photos/Wemon_Shirts/' + key
#
# if not isExist:
#     # Create a new directory because it does not exist
#     os.makedirs('./Photos/Wemon_Shirts/' + key)
#     file_path = './Photos/Wemon_Shirts/' + key
#     print("The new directory is created!")
# csv_file = "category_wemon_shirts.csv"
# download_images(csv_file, file_path)
