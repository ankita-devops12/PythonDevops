import json
import pdb
from sys import exception


#Read log file
def read_logs():
    try:
        with open("app.log","r") as files:
            return files.readlines()
    except FileNotFoundError:
        print("file not found error")
        return []
    except Exception as e:
        print("error occured:",e)
        return []


#analize fie and return count
def analyze(lines):
    # pdb.set_trace()
    log_count = {
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO":log_count["INFO"]+1})
        elif "WARNING" in line:
            log_count.update({"WARNING": log_count["WARNING"] + 1})
        elif "ERROR":
            log_count.update({"ERROR": log_count["ERROR"] + 1})
        else:
            pass
    return log_count


#Write log count in JSON file
def writelogcount():
    try:
        with open("logcount.json","w+") as file:
            json.dump(count,file)
    except Exception as e:
        print("error occured:",e)
lines = read_logs()
count=analyze(lines)
print(count)
writelogcount()
