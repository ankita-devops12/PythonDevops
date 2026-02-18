import json
import pdb
from sys import exception

from day4_task_loganalyzer import lines


class LogAnalyzer:
    #Automatically call when objects are created
    def __init__(self,file_name, output_file):
        self.file_name=file_name
        self.output_file=output_file

    #Read log file
    def read_logs(self):
        with open(self.file_name,"r") as files:
            return files.readlines()

    # Write log count in JSON file
    def write_JSON(self,count):
        with open(self.output_file, "w+") as file:
            json.dump(count, file)

    #analize fie and return count
    def analyze(self):
        # pdb.set_trace()
        log_count = {
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }
        lines=self.read_logs()
        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO":log_count["INFO"]+1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"] + 1})
            elif "ERROR":
                log_count.update({"ERROR": log_count["ERROR"] + 1})
            else:
                pass
        self.write_JSON(log_count)

log1=LogAnalyzer("app.log","logfileoutput.json")
log_count=log1.analyze()
