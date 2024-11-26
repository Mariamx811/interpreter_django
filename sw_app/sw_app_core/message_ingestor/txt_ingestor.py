from .message_ingestor import MessageIngestor
import json

"""It reads data from txt file

params:

file_path : the path to the file that holds the data

return:

a list of dictionaries (the data in a list)
"""

class TxtIngestor(MessageIngestor):

    def read_data(self, file_path):
        data = []
        with open(file_path,"r") as file:
            for line in file:
                data.append(json.loads(line.strip()))
        return data


