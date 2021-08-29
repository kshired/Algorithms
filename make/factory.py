from baekjoon import Baekjoon
from programmers import Programmers

def factory(choice,problem_number):
    if not problem_number.isdigit():
        raise ValueError('문제 번호는 정수여야합니다.')
    
    if choice == 1:
        return Baekjoon(problem_number)
    elif choice == 2:
        return Programmers(problem_number)
    else:
        raise ValueError('사이트는 1과 2중에서 골라야합니다.')
    