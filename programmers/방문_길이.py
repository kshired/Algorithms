# https://programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

def solution(dirs):
    d = {'U':(1,0),'D':(-1,0),'R':(0,1),'L':(0,-1)}
    visit = set()
    y,x = 0,0
    
    for dir in dirs:
        dy,dx = d[dir][0]+y, d[dir][1]+x
        if -5 <= dy <= 5 and -5 <= dx <= 5:
            visit.add((y,x,dy,dx))
            visit.add((dy,dx,y,x))
        else:
            dy,dx = y,x
        y,x = dy,dx
    
    return len(visit)//2