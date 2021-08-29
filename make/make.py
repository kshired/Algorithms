from factory import factory

choice = int(input('사이트를 선택해주세요\n1. 백준\n2. 프로그래머스\n입력 : '))
problem_number = input('문제 번호를 입력해주세요 : ')

site = factory(choice,problem_number)

try:
    f = open(site.get_filename(),'x')
    f.write(site.get_content())
except:
    raise FileExistsError(f'이미 [{problem_number}. {site.get_title()}] 파일이 존재합니다!')

f.close()
print(f'[{problem_number}번: {site.get_title()}] 문제의 코드가 생성되었습니다.')