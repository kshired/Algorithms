# Topological Sort

- 위상 정렬은 그래프 중에서도 DAG에서 사용가능한 알고리즘.
- DAG는 Directed Acyclic Graph이며, 사이클이 없는 유향 그래프를 의미.
- 유향 그래프의 방향성을 거스르지 않게 정점들을 나열 하는 것.
- 어떤 일을 수행하기 전, 미리 해야 할 일이 있으면, 미리 수행 해야 할 일을 먼저하는 것과 같음.

**DFS를 활용하는 방법**

- DFS를 실행하면서, DFS가 끝나는 순서의 역순이 위상 정렬의 결과가 됨.
- DFS가 끝날 때 마다 스택에 넣고, 결과를 출력 할 때 스택에서 하나씩 거내면서 출력해주면 됨.

```cpp
#include <bits/stdc+-+.h>
#define N 1000
using namespace std;

vector<int> g[N+1];
stack<int> s;
vector<bool> visited(N+1);

void dfs(int v){
  visited[v] = true;
  for(int i=0; i<g[v].size(); i++){
    if(!visited[ g[v][i] ]) dfs(i);
  }
  s.push(v);
}
```

```python
from collections import deque

N = 1000
s = deque()
g = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

def dfs(v):
	visited[v] = True
	for i in range(len(g[v])):
		if not visited[g[v][i]]:
			dfs(i)
	s.append(v)
```

**BFS와 in-degree 활용**

- 먼저 간선의 정보를 입력받고, in-degree가 0인 정점을 모두 큐에 삽입
- in-degree가 0이라는 것은, 위상 정렬 결과에서 맨 앞에 나올 수 있다는 것
- 정점의 개수만큼 큐가 빌 때까지, 아래 작업을 반복
  - 큐에서 맨 앞에 있는 정점과 그 정점에서 뻗어 나가는 간선들을 그래프에서 제거
  - 위 동작으로 인해 in-degree가 0이 된 정점을 큐에 삽입

[https://www.acmicpc.net/problem/1766](https://www.acmicpc.net/problem/1766) 에서는 숫자가 작은 문제집을 먼저 풀라고 했기 때문에 작은 것부터 출력을 해야 함.

그럴 때에는 priority_queue를 써서 작은 값부터 출력을 하면 됨.

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> g[32010];
vector<int> indegree(32010);
priority_queue<int> pq; // max heap

int main(){
	scanf("%d %d", &n, &m);
	for(int i=0; i<m; i++){
		int a, b; scanf("%d %d", &a, &b);
		g[a].push_back(b);
		indegree[b]++;
	}
	for(int i=1; i<=n; i++) if(!indegree[i]) pq.push(-i);
	while(!pq.empty()){
		int poped = -pq.top(); pq.pop();
		printf("%d ", poped);
		for(int i=0; i<g[poped].size(); i++){
			int nxt = g[poped][i];
			indegree[nxt]--;
			if(!indegree[nxt]) pq.push(-nxt);
		}
	}
}
```

```python
import heapq,sys

input = lambda: sys.stdin.readline().rstrip()

N,M = map(int,input().split())

g = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
pq = [] # mean heap

for i in range(M):
	s,e = map(int,input().split())
	g[s].append(e)
	indegree[e] += 1

for i in range(1,N+1):
	if indegree[i] == 0:
		heapq.heappush(pq,i)

while pq:
	poped = heapq.heappop(pq)
	print(poped,end = ' ')
	for i in g[poped]:
		indegree[i] -= 1
		if indegree[i] == 0:
			heapq.heappush(pq,i)
```
