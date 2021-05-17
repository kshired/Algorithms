import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
INF = 10e+9

N = int(input())
M = int(input())


hq = [] # 우선 순위 큐
graph = [[] for _ in range(N+1)]
path = [0 for _ in range(N+1)] # 최단 경로 저장

# 최단거리를 전부 무한대로 초기화
dist = [INF for _ in range(N+1)]

# 그래프 초기화
for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start,end = map(int,input().split())

# 출발점부터 시작하며, 자기 자신과의 거리는 0
heapq.heappush(hq,(0,start))

while hq:
    # 시작점으로부터 최소 거리의 정점과 정점의 가중치를 가져옴
    weight, now = heapq.heappop(hq)

    # 정점의 가중치가 구해져있는 최단거리보다 길면 무시
    if weight > dist[now]:
        continue

    # 우선순위큐에서 가져온 정점을 이용하여 최단거리 갱신
    for i in graph[now]:
        nxt = i[0]
        nxtWeight = weight + i[1]
        if dist[nxt] > nxtWeight:
            dist[nxt] = nxtWeight
            path[nxt] = now # now를 거쳐서 nxt로 가는 것이 최단 경로라면 path[nxt] = now로 해서 이전 정점 저장
            heapq.heappush(hq,(nxtWeight,nxt))

print(dist[end])

# 도착 정점에서 path 배열을 따라 역추적
res = []
while True:
    res.append(end)
    end = path[end]
    if end == start:
        res.append(end)
        break

print(len(res))

for i in res[::-1]:
    print(i,end=' ')
print()