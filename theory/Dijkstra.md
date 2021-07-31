# Dijkstra Algorithm

한 정점에서 다른 모든 정점까지의 최단 경로를 구하는 알고리즘.

그리디를 기반으로 작동하며, 음수 간선이 있는 경우 사용 불가능

**동작방식**

처음에 시작 정점까지의 거리를 0, 다른 모든 정점까지의 거리를 INF로 초기화함. 아직 방문하지 않았음을 나타내는 것.

최단 경로를 확정하기 전까지 아래 과정을 반복

1. 현재 정점과 인접한 모든 정점들을 반복하면서 거리를 갱신. 현재 정점까지의 최단 거리를 A, 현재 인접한 정점 I를 잇는 간선의 가중치를 B, 지금까지 구한 I 까지의 최단 거리를 C라고 할 때, A + B < C 이면 최단거리를 A + B로 갱신.
2. 거리가 확정되지 않은 정점 중 가장 짧은 거리의 정점으로 이동, 해당 정점의 최단거리를 확정시킴. 더 이상 그 정점의 최단거리가 갱신 될 일이 없음을 의미

O(V^2) 구현

```cpp
#include <vector>
#include <utility>
#define x first
#define y second
using namespace std;

typedef pair<int, int> p;

vector<p> g[20001]; //인접 리스트
int dist[20001]={0}; //최단 거리
int chk[20001]={0}; //거리 확정 여부

//거리 초기화, 현재 정점은 시작 정점으로 초기화
for(int i=1; i<=v; i++) dist[i] = 1e9+7;
dist[start] = 0; chk[start] = 1;
now = start;

//V번 반복(모든 정점을 하나씩 거리 확정)
for(int aaa=0; aaa<v; aaa++){
    //인접한 모든 정점 방문
    for(auto i : g[u]){
    	int nxt = i.x;
    	int edgeCost = i.y;
        if(!chk[nxt]){
            if(dist[nxt] > dist[now] + edgeCost){
                dist[nxt] = dist[now] + edgeCost;
            }
        }
    }

    //최단 거리 확정
    chk[now] = 1;

    //7. 거리 미확정 정점 중, 출발점으로부터의 거리가 가장 작은 정점 선택
    int min = 1e9 + 7;
    for(int i=1; i<=v; i++){
        if(!chk[i]){
            if(dist[i] < min){
                min = dist[i];
                now = i;
            }
        }
    }
}
```

```python
INF = 123456789

graph = [[] for _ in range(N+1)]
dist = [0 for _ in range(N+1)]
chk = [False for _ in range(N+1)]

for i in range(1,V+1):
    dist[i] = INF
dist[start] = 0
chk[start] = True
now = start

for _ in range(V):
    for i in graph[now]:
        nxt = i[0]
        weight = i[1]
        if not chk[nxt]:
            dist[nxt] = min(dist[nxt], dist[now] + weight)

    chk[now] = True

    minimum = INF
    for i in range(1,V+1):
        if not chk[i]:
            if dist[i] < minimum:
                minimum = dist[i]
                now = i
```

Priority Queue

```python
# https://acmicpc.net/problem/1753
# 최단경로

import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

INF = 10e+9
V, E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
dist = [0 for _ in range(V+1)]

# 그래프 초기화
for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

# 최단거리를 전부 무한대로 초기화
for i in range(1,V+1):
    dist[i] = INF

# 출발점 자기 자신과의 거리는 0
dist[start] = 0

# 우선 순위 큐
hq = []

# 출발점부터 시작
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
        nxtWeight = weight + i[1] # 현재 정점으로부터 연결 된 정점의 가중치 + 시작점 ~ 현재 정점의 가중치
        if nxtWeight < dist[nxt]:
            dist[nxt] = nxtWeight
            heapq.heappush(hq,(nxtWeight,nxt))

for i in dist[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)
```

**경로 역추적**

```python
# https://acmicpc.net/problem/11779
# 최소비용 구하기 2

import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
INF = 10e+9

N = int(input())
M = int(input())

hq = []
graph = [[] for _ in range(N+1)]
path = [0 for _ in range(N+1)] # 최단 경로 저장
dist = [INF for _ in range(N+1)]

for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start,end = map(int,input().split())

heapq.heappush(hq,(0,start))

while hq:
    weight, now = heapq.heappop(hq)

    if weight > dist[now]:
        continue

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
```
