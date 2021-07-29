# Stack

- <strong>후입선출(Last In First Out, LIFO)</strong>의 형태를 가진 자료구조

- 데이터의 개수가 스택의 크기를 초과하면 overflow가 일어나고, 아무것도 없을 때 pop을 하거나 데이터에 접근시 underflow가 일어나기 때문에 구현시 예외처리가 필수적

구현

```c
#include <stdio.h>
#include <stdlib.h>

#define size 100

int stack[size];
int top=-1;

void push(int item){
    if(top>=size-1){
        printf("\n\nStack is FULL\n");
        exit(1);
    }
    else stack[++top]=item;
}

int pop(){
    if(top==-1){
        printf("\n\nStack is Empty\n");
        exit(1);
    }
    else return stack[top--];
}

void del(){
    if(top==-1){
        printf("\n\nStack is Empty\n");
        exit(1);
    }
    else top--;
}

int peek(){
    if(top==-1){
        printf("\n\nStack is Empty\n");
        exit(1);
    }
    else return stack[top];
}

```

```python
'''
파이썬에서는 list를 이용하여 쉽게 스택을 구현 할 수 있으며
실제 사용시에는 collections에 구현되어 있는 deque를 이용하면 더 빠름

from collections import deque
dq = deque()

# 스택으로 사용시
dq.append() # 가장 오른쪽에 추가
dq.pop() # 가장 오른쪽 원소 삭제 및 반환

# 큐로 사용시
dq.append() # 가장 오른쪽에 추가
dq.popleft() # 가장 왼쪽 원소 삭제 및 반환
'''

stack = []
stack.append(1) # push
stack.append(2)
stack.pop() # pop, 2
stack[-1] # top, 1
len(stack) # size, 1

'''
그냥 list의 append와 pop만을 사용하면, stack과 동일하게 동작
'''
```

ex) C++ STL 사용하기

- empty() - 스택이 비어있으면 true, 비어있지 않으면 false을 반환합니다.
- size() - 스택에 있는 데이터의 개수를 반환합니다.
- top() - 스택의 맨 위에 있는 값(가장 나중에 넣은 값)을 반환합니다.
- push(data) - 스택에 data를 삽입합니다.
- pop() - 스택에서 데이터를 제거합니다.

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int n;
stack<int> s;

int main(){
	cin >> n;
	while(n--){
		string op;
		cin >> op;
		if(op == "push"){
			int x; cin >> x;
			s.push(x);
		}
		else if(op == "pop"){
			if(s.empty()) cout << -1 << "\n";
			else{
				cout << s.top() << "\n";
				s.pop();
		    }
		}
		else if(op == "size"){
			cout << s.size() << "\n";
        }
		else if(op == "empty"){
			cout << s.empty() << "\n";
		}
		else if(op == "top"){
			if(s.empty()) cout << -1 << "\n";
			else cout << s.top() << "\n";
		}
	}
}
```
