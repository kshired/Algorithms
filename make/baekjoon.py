import os
import re
from base_site import BaseSite

class Baekjoon(BaseSite):
    def __init__(self,problem_number):
        super().__init__('https://acmicpc.net/problem',problem_number)
        self.set_title()
    
    def set_title(self):
        title = re.search('(?<=<title>).+?(?=</title>)', self.response.text, re.DOTALL).group().strip().split(':')[1].strip()
        self.title = title
    
    def get_title(self):
        return self.title
    
    def get_filename(self):
        return f'{os.path.dirname(__file__)}/../baekjoon/{self.problem_number}.py'
    
    def get_content(self):
        return f'# {self.url}\n# {self.title}\n\nimport sys\ninput = lambda : sys.stdin.readline().rstrip()\ninput_multiple_int = lambda : map(int,input().split())\n'