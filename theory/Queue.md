# Queue

- <strong>선입선출(First In First Out, FIFO)</strong>의 형태를 가지고 있는 자료구조
- 먼저 온 것이 먼저 나가는 특성을 가지는 것이, 줄을 서서 기다릴 때 먼저 온 사람이 먼저 들어가는 것과 같은 이치

구현

```cpp
#include <stdio.h>
#include <string.h>

#define SIZE 10010

int q[SIZE];
int front = 0;
int rear = 0;

void push(int data){
    q[rear++] = data;
}

int pop(){
    if(front >= rear) return -1;
    return q[front++];
}

int size(){
    return rear-front;
}

int empty(){
    if(front >= rear) return 1;
    return false;
}

int getFront(){
    if(front >= rear) return -1;
    return q[front];
}

int getBack(){
    if(front >= rear) return -1;
    return q[rear-1];
}

int main(){
    int n; scanf("%d", &n);
    while(n--){
        char op[10]; scanf("%s", op);
        if(!strcmp(op, "push")){
            int data; scanf("%d", &data);
            push(data);
        }else if(!strcmp(op, "pop")){
            printf("%d\n", pop());
        }else if(!strcmp(op, "size")){
            printf("%d\n", size());
        }else if(!strcmp(op, "empty")){
            printf("%d\n", empty());
        }else if(!strcmp(op, "front")){
            printf("%d\n", getFront());
        }else if(!strcmp(op, "back")){
            printf("%d\n", getBack());
        }
    }
}
```

```python
'''
stack과 마찬가지로 파이썬에서는 list를 이용하여 쉽게 구현 할 수 있다.
하지만 이 또한 deque를 사용하는 것이 빠르고 쉽다.
from collections import deque
dq = deque()

# 스택으로 사용시
dq.append() # 가장 오른쪽에 추가
dq.pop() # 가장 오른쪽 원소 삭제 및 반환

# 큐로 사용시
dq.append() # 가장 오른쪽에 추가
dq.popleft() # 가장 왼쪽 원소 삭제 및 반환
'''

queue = []
queue.append(1) # 가장 오른쪽에 원소 추가 push
queue.append(2) # 가장 오른쪽에 원소 추가 push
queue.pop(0)    # 가장 왼쪽 원소 삭제 및 반환, pop, 1
len(queue)      # size 및 empty 판단
queue[0]        # 제일 앞의 원소를 읽기, getFront
queue[-1]       # 제일 마지막의 원소를 읽기, getBack
```

ex) C++ STL

- empty() - 큐가 비어있으면 true, 그렇지 않으면 false를 반환합니다.
- size() - 큐에 있는 데이터의 개수를 반환압니다.
- front() - 큐에 가장 처음으로 들어간 값을 반환합니다.
- back() - 큐에 가장 마지막으로 들어간 값을 반환합니다.
- push(data) - 큐에 data를 삽입합니다.
- pop() - 큐에서 데이터를 제거합니다.

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int n;
queue<int> q;

int main(){
	cin >> n;
	while(n--){
		string op;
		cin >> op;
		if(op == "push"){
			int x; cin >> x;
			q.push(x);
		}
		else if(op == "pop"){
			if(q.empty()) cout << -1 << "\n";
			else{
				cout << q.front() << "\n";
				q.pop();
		  }
		}
		else if(op == "size"){
			cout << q.size() << "\n";
        }
		else if(op == "empty"){
			cout << q.empty() << "\n";
		}
		else if(op == "front"){
			if(q.empty()) cout << -1 << "\n";
			else cout << q.front() << "\n";
		}
		else if(op == "back"){
			if(q.empty()) cout << -1 << "\n";
			else cout << q.back() << "\n";
		}
	}
}
```
