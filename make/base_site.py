import requests

class BaseSite:
    def __init__(self,url,problem_number):
        self.url = url
        self.problem_number = problem_number
        self.response = requests.get(f'{url}/{problem_number}')
        self.title = None
    
    def __set_title(self):
        pass
    
    def get_title(self):
        pass

    def get_filename(self):
        pass

    def get_content(self):
        pass