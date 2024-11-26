import os
from .txt_ingestor import TxtIngestor


""" Factory class to determine what file type to use (.txt, .csv ..etc)"""
class IngestorFactory:

    def __init__(self,file_path):
        self.file_path = file_path

    """Function to create an object of the right type according to file extensions"""
    def get_data_ingestor(self):
        """Getting the file extension to call the suitable ingestor"""
        _, file_extension = os.path.splitext(self.file_path)
        
        if file_extension == ".txt":
            return TxtIngestor()   
    
        