import os

from pandas import read_csv


def getDuplicatesWithCount(listOfElems):
    ''' Get frequency count of duplicate elements in the given list '''
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1

            # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
    dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}
    # Returns a dict of duplicate elements and thier frequency count
    return dictOfElems

datas = read_csv("category_wemon_shirts.csv")
data = datas['urls'].tolist()
names = [(item.split("/")[-1]) for item in data]
i = 0
dictOfElems = getDuplicatesWithCount(names)
print(type(dictOfElems.items()))
for key, value in dictOfElems.items():
    isExist = os.path.exists('./Photos/Wemon_Shirts/'+key)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs('./Photos/Wemon_Shirts/'+key)
        print("The new directory is created!")
    i = i+1
    print(key , ' :: ', value)