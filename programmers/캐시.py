# https://programmers.co.kr/learn/courses/30/lessons/17680
# 캐시

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    
    cache = []
    answer = 0
    
    for city in cities:
        if city.upper() in cache:
            answer += 1
            cache.remove(city.upper())
            cache[0:0] = [city.upper()]
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop()
                cache[0:0] = [city.upper()]
            else:
                cache[0:0] = [city.upper()]
        
    return answer