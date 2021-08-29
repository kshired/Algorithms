import os
import re
from base_site import BaseSite

class Programmers(BaseSite):
    def __init__(self,problem_number):
        super().__init__('https://programmers.co.kr/learn/courses/30/lessons',problem_number)
        self.set_title()
    
    def set_title(self):
        title = re.search('(?<=<title>).+?(?=</title>)', self.response.text, re.DOTALL).group().strip()
        title = re.search('[-](.*?)[|]',title,re.DOTALL).group().strip()[2:-2]
        self.title = title
    
    def get_title(self):
        return self.title
    
    def get_filename(self):
        file_name = re.sub(r'\s','_',self.title)
        return f'{os.path.dirname(__file__)}/../programmers/{file_name}.py'
    
    def get_content(self):
        return f'# {self.url}\n# {self.title}\n'