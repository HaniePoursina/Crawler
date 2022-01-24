import os
import pandas as pd
df =  pd.read_csv("category_wemon_shirts.csv")
urls = df["urls"]
images = df["images"]
filter_cap = []


# for names in urls:
#     filter_cap.append(names.split("/")[-1]+".jpg" )
# # for image in images:
# #     filter_cap.append(image.split("/")[-1]+".jpg" )
# df["path"] = filter_cap
# df.to_csv("category_wemon_shirts.csv", index= False)
# # Function to rename multiple files
# folder = './Photos/Wemon_Shirts'
# for count,filename in enumerate(os.listdir(folder)):
#     dst = filter_cap[count]
#     src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
#     dst = f"{folder}/{dst}"
#     print(dst)
#     # rename() function will
#     # rename all the files
#     os.rename(src, dst)
