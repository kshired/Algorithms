# Floyd Warshall Algorithm

플로이드 와샬 알고리즘은 모든 정점에서 다른 모든 정점까지의 최단 거리를 모두 구하는 알고리즘.

### **작동 방법**

DP를 기반으로 작동하며,

dp[i][j] = i에서 j까지의 최단 거리라고 정의.

3중 for문을 돌리는데, 반복되는 변수를 i, j, k로 하고 각각 시작 정점, 도착 정점, 경유 정점으로 사용.

i에서 j로 바로 가는 것보다, i에서 k를 거쳐서 j로 가는 것이 빠르다면 갱신.

```python
INF = 1e9+7
N = 100
graph = [[INF for in range(N)] for _ in range(N)]

def floyd_warshall(graph):
    for i in range(N):
        graph[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]: # min 함수를 쓰는 것보다 속도가 빠름
                    graph[i][j] = graph[i][k]+graph[k][j]
```
