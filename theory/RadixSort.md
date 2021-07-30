# Radix Sort

Radix Sort는 특수한 경우에만 성립하며, 이 특수한 경우에는 앞서 공부한 다른 정렬 알고리즘 보다 꽤나 괜찮은 성능을 보여주는 정렬 알고리즘임.

- 낮은 자리수부터 비교하여 정렬하는 알고리즘
- 정수 데이터에서만 성립
- 몇 개의 키 ( 자리수 ) 를 기준으로 정렬이 진행 됨

ex)

```
170 45 75 90 2 24 802 66
-> 1의 자리만 보고 정렬, 1의 자리가 같은 값이면 먼저 나온 것이 앞
170 90 2 802 24 45 75 66
-> 10의 자리에 대해 정렬
2 802 24 45 66 170 75 90
-> 100의 자리에 대해 정렬
2 24 45 66 75 90 170 802
-> 정렬 완료
```

구현 시에는 Queue를 사용하며, 정수의 자리 수를 기준으로 큐에 넣은 후 빼는 방식을 사용

```
35 31 55 41 54 49
-> 0 ~ 9번까지의 큐를 생성
1의 자리를 기준으로 큐에 삽입
1 : 31, 41
4: 54
5: 35, 55
9: 49
-> 이제 큐에서 차례대로 꺼내면
31 41 54 35 55 49
-> 다시 10의 자리를 기준으로 큐에 삽입
3: 31, 35
4: 41, 49
5: 54, 55
-> 큐에서 차례대로 꺼내면
31, 35, 41, 49, 54, 55
```

구현

```cpp
#include <cstdio>
#include <queue>

using namespace std;
const int n = 6;

void radixSort(int arr[]){
	queue<int> q[10]; // 각 자리수 저장하는 큐
	int cnt = 1; // 최대 길이^10
	int max = arr[0];

	for(int i=1;i<n;++i){
		max = max > arr[i] ? max : arr[i];
	}
	// 최댓값을 이용하여 가장 긴 길이 구하기

	while(max>0){
		cnt *= 10;
		max /= 10;
	}

	for(int i=1;i<cnt;i*=10){ // 정렬 할 자리수만큼 for문
 		for(int j=0;j<n;++j){ // 각 각의 큐에 저장
			int k = (arr[j]%(i*10))/i;
			q[k].push(arr[j]);
		}

		int idx = 0;

		for(int j=0;j<10;++j){  // 각 자리수에 맞게 정렬 된 데이터 가져오기
			while(!q[j].empty()){
				arr[idx++] = q[j].front();
				q[j].pop();
			}
		}
	}
}

int main(){
    int arr[n] = {32, 1374, 1, 84, 70,124};
    radixSort(arr);
    for(int i=0; i<n; i++) printf("%d ", arr[i]);
}
```

```python
from collections import deque

def radix_sort(arr):
    dq = [deque() for _ in range(10)]
    cnt = len(str(max(arr)))

    for i in (10 ** x for x in range(cnt-1)):
        for j in range(len(arr)):
            k = (arr[j]%(i*10))//i
            dq[k].append(arr[j])
        idx = 0

        for j in range(10):
            while dq[j]:
                arr[idx] = dq[j].popleft()
                idx += 1

arr = [32, 1374, 1, 84, 70,124]
radix_sort(arr)
print(arr)
```

시간 복잡도

- 최대 값 구할 때 $O(n)$
- 최대값이 몇 자리인지 구할 때 $O(logMAX)$, 이 값을 $d$라고하면 $O(d)$
- 바깥 for문은 $d$ 번, 안쪽은 $n$번 이므로
- 최종은 $O(n+d+dn) = O(dn)$
