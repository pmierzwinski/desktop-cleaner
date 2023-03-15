import glob
import os

STRING_MAPER = {}

def addNewStingMapper(string):
    if (len(STRING_MAPER) == 0):
        STRING_MAPER[string] = 1
        return 1

    last_index = max(STRING_MAPER, key=STRING_MAPER.get)
    new_index = int(STRING_MAPER[last_index]) + 1
    STRING_MAPER[string] = new_index
    return new_index

def getStringNumericIndex(string):
    if string in STRING_MAPER:
        return STRING_MAPER[string]
    return addNewStingMapper(string)

def getFolderNames(folder_path):
    files = glob.glob(folder_path, recursive=True)
    folder_names = []
    for f in files:
        file_path, file_extension = os.path.splitext(f)
        folder_names.append(os.path.basename(file_path))
    return folder_names

folder_path = "C:/Users/xxx/Desktop/AI_TRAIN2/"
test = getFolderNames(folder_path + "*")
data_map = {}

for folder_name in test:
    folder_data = []
    files = glob.glob(folder_path + folder_name +"/*", recursive=True)
    for f in files:
        data = []
        file_path, file_extension = os.path.splitext(f)
        file_stats = os.stat(f)
        data.append(getStringNumericIndex(
            os.path.basename(file_path)
        ).__str__())
        data.append(getStringNumericIndex(
            file_extension
        ).__str__())
        data.append(file_stats.st_size.__str__())
        folder_data.append(data)
    data_map[folder_name] = folder_data

print(STRING_MAPER)

with open('folder.data', 'w') as f:
    f.write("name,extension,size,output\n")
    for folder, data in data_map.items():
        for file_data in data:
            f.write(','.join(file_data) + "," + folder)
            f.write("\n")

