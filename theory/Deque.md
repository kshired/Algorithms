# Deque ( Double Ended Queue )

스택과 큐와 달리 양쪽 모두 삽입과 삭제가 가능한 자료구조

```c
#include <stdio.h>
#include <string.h>
#define SIZE 50010

int dq[SIZE];
int head = 20000, rear = 20000;

void push_front(int data){
    dq[--head] = data;
}

void push_back(int data){
    dq[rear++] = data;
}

int pop_front(){
    if(head >= rear) return -1;
    return dq[head++];
}

int pop_back(){
    if(head >= rear) return -1;
    return dq[--rear];
}

int size(){
    return rear - head;
}

int empty(){
    return head == rear;
}

int front(){
    if(head >= rear) return -1;
    return dq[head];
}

int back(){
    if(head >= rear) return -1;
    return dq[rear-1];
}

int main(){
    int n; scanf("%d", &n);
    while(n--){
        char op[20]; scanf("%s", op);
        if(!strcmp(op, "push_front")){
            int data; scanf("%d", &data);
            push_front(data);
        }else if(!strcmp(op, "push_back")){
            int data; scanf("%d", &data);
            push_back(data);
        }else if(!strcmp(op, "pop_front")){
            printf("%d\n", pop_front());
        }else if(!strcmp(op, "pop_back")){
            printf("%d\n", pop_back());
        }else if(!strcmp(op, "size")){
            printf("%d\n", size());
        }else if(!strcmp(op, "empty")){
            printf("%d\n", empty());
        }else if(!strcmp(op, "front")){
            printf("%d\n", front());
        }else if(!strcmp(op, "back")){
            printf("%d\n", back());
        }
    }
}
```

ex) C++ STL

- empty() - 덱이 비어있으면 true, 그렇지 않으면 false를 반환합니다.
- size() - 덱에 있는 데이터의 개수를 반환합니다.
- front() - 덱의 맨 앞에 있는 데이터를 반환합니다.
- back() - 덱의 맨 뒤에 있는 데이터를 반환합니다.
- push_front(data) - 덱의 맨 앞에 data를 삽입합니다.
- push_back(data) - 덱의 맨 뒤에 data를 삽입합니다.
- pop_front() - 덱의 맨 앞에 있는 데이터를 삭제합니다.
- pop_back() - 덱의 맨 뒤에 있는 데이터를 삭제합니다.

```c
#include <deque>
using namespace std;

deque<int> dq;
```

```python
# python에서는 collections의 deque를 사용하면 된다
from collections import deque
dq = deque()

dq.append(x) # 오른쪽(끝)에 삽입
dq.appendleft(x) # 왼쪽(앞)에 삽입
dq.extend(iterable) # iterable arguments를 오른쪽(끝)에 삽입
dq.extendleft(iterable) # iterable arguments를 왼쪽(앞)에 삽입.
# 'de'를 삽입하면, 'e','d' 순서로 삽입된다
dq.pop() # 오른쪽(끝)에서 제거와 반환
dq.popleft() # 왼쪽(앞)에서 제거와 반환
dq.rotate(n) # n번만큼 elements를 이동시켜주는 method. 양수면 오른쪽으로, 음수면 왼쪽으로 rotate
```
