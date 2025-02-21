import os
import glob

STRING_MAPPER = {}

def addNewStringMapper(string):
    if len(STRING_MAPPER) == 0:
        STRING_MAPPER[string] = 1
        return 1
    last_index = max(STRING_MAPPER, key=STRING_MAPPER.get)
    new_index = int(STRING_MAPPER[last_index]) + 1
    STRING_MAPPER[string] = new_index
    return new_index

def getStringNumericIndex(string):
    if string in STRING_MAPPER:
        return STRING_MAPPER[string]
    return addNewStringMapper(string)

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
    files = glob.glob(f"{folder_path}{folder_name}/*", recursive=True)
    for f in files:
        data = []
        file_path, file_extension = os.path.splitext(f)
        file_stats = os.stat(f)
        data.append(str(getStringNumericIndex(os.path.basename(file_path))))
        data.append(str(getStringNumericIndex(file_extension)))
        data.append(str(file_stats.st_size))
        folder_data.append(data)
    data_map[folder_name] = folder_data

print(STRING_MAPPER)

with open('folder.data', 'w') as f:
    f.write("name,extension,size,output\n")
    for folder, data in data_map.items():
        for file_data in data:
            f.write(','.join(file_data) + f",{folder}\n")