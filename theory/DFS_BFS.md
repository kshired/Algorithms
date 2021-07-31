# DFS와 BFS

- DFS

  - Depth First Search ( 깊이 우선 탐색 )
  - 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
  - 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방향으로 다시 탐색을 진행하는 방법과 유사함
  - 넓게(wide) 탐색하기 전에 깊게(deep) 탐색함
  - 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함
  - 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 좀 더 간단함
  - 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느림

  ```
  1. 시작 정점을 "방문 했음"으로 설정
  2. 인접한 정점에서 아직 방문하지 않은 정점을 시작 정점으로 잡은 뒤 1번 다시 실행(재귀 호출)
  3. 인접한 정점 중 더 이상 방문하지 않은 정점이 없다면 이전 정점으로 돌아가서 2번 실행
  4. 모든 정점 방문 완료시 탐색 종료
  ```

  ```c
  int map[1001][1001] = {0}, visit[1001];
  //map : 인접 행렬, visit : 방문 체크

  void dfs(int v){
  	visit[v] = 1;
  	printf("%d ", v);
  	for(int i=1;i<=1000;++i){
  		if(map[v][i] == 1 && !visit[i]){
  			dfs(i);
  		}
  	}
  }
  ```

  ```python
  def dfs(v):
  	global graph,visit
  	visit[v] = 1
  	print(v)
  	for i in range(len(graph)):
  		if graph[v][i] == 1 and visit[i] == 0 :
  			dfs(i)

  '''
  6-4-5 - 1
  	| | /
  	3-2

  dfs => 1-2-3-4-5-6
  '''
  graph = [
      [0,0,0,0,0,0,0],
      [0,0,1,0,0,1,0],
      [0,1,0,1,0,1,0],
      [0,0,1,0,1,0,0],
      [0,0,0,1,0,1,1],
      [0,1,1,0,1,0,0],
      [0,0,0,0,1,0,0],
  ]

  visit = [ 0 for _ in range(7) ]

  dfs(1)
  ```

- BFS

  - Breadth First Search ( 너비 우선 탐색 )
  - 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법이다.
  - 즉, 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것.
  - 두 노드 사이의 최단 경로 또는 임의의 경로를 찾고 싶을 때 사용
  - 재귀적으로 동작하지 않음
  - 어떤 노드를 방문했었는지 여부를 반드시 검사해야 함
  - 큐를 사용한다

  ```c
  int map[1001][1001]={0}, visit1[1001];
  int q[1001];
  int front=0, rear=0;

  void bfs(int v){
  	visit1[v] = 1;
  	printf("%d ", v);
  	q[rear++] = v;
  	while(front < rear){
  		v = q[front++];
  		for(int i=1; i<=n; i++){
  			if(map[v][i]==1 && !visit1[i]){
  				visit1[i] = 1;
  				printf("%d ", i);
  				q[rear++] = i;
  			}
  		}
  	}
  }
  ```

  ```python
  from collections import deque
  q = deque()

  def bfs(v):
  	global q,visit,graph
  	visit[v] = 1
  	print(v)
  	q.append(v)
  	while q:
  		v = q.popleft()
  		for i in range(len(graph)):
  			if graph[v][i] == 1 and visit[i] == 0:
  				visit[i] = 1
  				print(i)
  				q.append(i)

  '''
  6-4-5 - 1
  	| | /
  	3-2

  bfs => 1-2-5-3-4-6
  '''
  graph = [
      [0,0,0,0,0,0,0],
      [0,0,1,0,0,1,0],
      [0,1,0,1,0,1,0],
      [0,0,1,0,1,0,0],
      [0,0,0,1,0,1,1],
      [0,1,1,0,1,0,0],
      [0,0,0,0,1,0,0],
  ]

  visit = [ 0 for _ in range(7) ]

  bfs(1)
  ```
