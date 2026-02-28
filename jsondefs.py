import json

def uploadData(data):
    try:
        with open ("data.json" , "w") as file :
            json.dump(data , file , indent=4)
    except FileNotFoundError:
        print("File does not exists ! \n")
        return 

def downloadData():
    try:
        with open ("data.json" , "r") as file :
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File does not exists ! \n")
        return []