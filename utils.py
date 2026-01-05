import os,json


def load_json(path,default):
    if not os.path.exists(path):
        return default
    
    with open(path,'r') as file:
        try:
             file_json_data = json.load(file)
             return file_json_data
        except Exception as e:
            print(f"Error Loading The File",e)
            return default
        
def save_json(path,data):
    folder_path = os.path.dirname(path)
    os.makedirs(folder_path,exist_ok=True)

    try:
         with open(path,'w')as file:
             json.dump(data,file,indent=4)
    except Exception as e:
             print("Error saving data to the file",e)
                 



