'''
findPrime(N:int) -> None
O(N^2)의 시간 복잡도로 N이하의 소수를 구하는 가장 쉬운 알고리즘.
'''
def findPrime(N):
    prime = []
    for i in range(2,N+1):
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            prime.append(i)

    for i in prime:
        print(i)

'''
findPrimeV2(N:int) -> None
O(NlogN)의 시간 복잡도로 N이하의 소수를 구하는 에라토스테네스의 체 알고리즘
'''
def findPrimeV2(N):
    prime = []
    isPrime = [True for _ in range(N+1)]
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2,N+1):
        if isPrime[i]:
            prime.append(i)
        for j in range(i*2,N+1,i):
            isPrime[j] = False
    
    for i in prime:
        print(i)

'''
findPrimeV3(N:int) -> None
2를 제외한 짝수를 먼저 False로 만들고,
그 후 홀수를 세면서 안쪽 for문은 sqrt(N)까지만 체크.
'''
def findPrimeV3(N):
    prime = []
    isPrime = [True for _ in range(N+1)]
    isPrime[0] = False
    isPrime[1] = False

    for i in range(4,N+1,2):
        isPrime[i] = False
    
    for i in range(3,N+1,2):
        if not isPrime[i]:
            continue
        prime.append(i)
        for j in range(i*i,N+1,i*2):
            isPrime[j] = False
    
    print(len(prime))
    