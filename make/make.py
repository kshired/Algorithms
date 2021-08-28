import os.path
import re
import requests

PROGRAMMERS_URL = 'https://programmers.co.kr/learn/courses/30/lessons/'
BAEKJOON_URL = 'https://acmicpc.net/problem/'

SITES =['','/../baekjoon/','/../programmers/']
URL = ''

SITE = int(input('사이트를 선택해주세요\n1. 백준\n2. 프로그래머스\n입력 : '))

if SITE == 1:
    URL = BAEKJOON_URL
elif SITE == 2:
    URL = PROGRAMMERS_URL
else:
    raise ValueError('사이트는 1과 2중에서 골라야합니다.')

NUMBER = input('문제 번호를 입력해주세요 : ')

if NUMBER.isdigit():
    URL += NUMBER
else:
    raise ValueError('문제 번호는 정수여야합니다.')

resp = requests.get(URL)
title = re.search('(?<=<title>).+?(?=</title>)', resp.text, re.DOTALL).group().strip()
if SITE == 1:
    title = title.split(':')[1].strip()
elif SITE == 2:
    title = re.search('[-](.*?)[|]',title,re.DOTALL).group().strip()[2:-2]

try:
    if SITE == 1:
        f = open(f'{os.path.dirname(__file__)}{SITES[SITE]}{NUMBER}.py','x')
        f.write(f'# {URL}\n# {title}\nimport sys\ninput = lambda : sys.stdin.readline().rstrip()\ninput_multiple_int = lambda : map(int,input().split())\n')
    elif SITE == 2:
        file_name = re.sub(r'\s','_',title)
        f = open(f'{os.path.dirname(__file__)}{SITES[SITE]}{file_name}.py','x')
        f.write(f'# {URL}\n# {title}')
except:
    raise FileExistsError(f'이미 [{NUMBER}. {title}] 파일이 존재합니다!')

f.close()
print(f'[{NUMBER}번: {title}] 문제의 코드가 생성되었습니다.')