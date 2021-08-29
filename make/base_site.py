import requests
from abc import *

class BaseSite(metaclass=ABCMeta):
    def __init__(self,url,problem_number):
        self.url = url
        self.problem_number = problem_number
        self.response = requests.get(f'{url}/{problem_number}')
        self.title = None
    
    @abstractmethod
    def set_title(self):
        pass
    
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass

    @abstractmethod
    def get_content(self):
        pass