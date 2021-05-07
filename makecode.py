import re
import requests

DEFAULT_URL = 'https://acmicpc.net/problem/'

NUMBER = input().rstrip()

URL = DEFAULT_URL+NUMBER

resp = requests.get(URL)
title = re.search('(?<=<title>).+?(?=</title>)', resp.text, re.DOTALL).group().strip().split(':')[1].strip()

f = open('./baekjoon/'+NUMBER+'.py','w')
f.write(f'''# {URL}
# {title}

import sys
input = lambda : sys.stdin.readline().rstrip()
''')
f.close()
print(f'{NUMBER}번 문제의 코드가 생성되었습니다.')