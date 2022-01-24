from pandas import read_csv
import pandas as pd
data = read_csv("category_wemon_shirts.csv")
images = data['image']
iamge_path = []
for image in images:
    filename = image.split("/")[-3] + ".jpg"
    iamge_path.append("./Photos/Wemon_Shirts" + filename)
dict = {'path': iamge_path}
df = pd.DataFrame(dict)
df.to_csv('category_wemon_shirts.csv', index=False)
