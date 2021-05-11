def solution(numbers, target):
    if not numbers:
        if target==0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[:-1],target-numbers[-1])+solution(numbers[:-1],target+numbers[-1])