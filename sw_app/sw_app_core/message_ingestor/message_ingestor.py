from abc import ABC, abstractmethod
import json

class MessageIngestor(ABC):

    """Class to read data from various sources"""
   
    @abstractmethod
    def read_data(self,**kwargs):
        pass


