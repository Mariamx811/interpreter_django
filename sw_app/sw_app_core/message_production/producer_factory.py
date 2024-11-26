import os
from .sqlite_producer import SqliteProducer

""" Factory class to determine what file type to use (.txt, .csv ..etc)"""
class ProducerFactory:

    def __init__(self,file_type):
        self.file_type = file_type

    def get_data_producer(self):

        if self.file_type == "sqlite":
            return SqliteProducer()   
    
        