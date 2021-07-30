# Counting Sort

0 이상의 정수 데이터가 각각 몇 번 나왔는지 카운팅하여 정렬하는 알고리즘

```
0, 1, 4, 3, 2, 0, 0, 4, 5, 2, 2, 3
-> 각 숫자가 몇 번 나왔는지 카운팅
0은 3번
1은 1번
2는 3번
3은 2번
4는 2번
5는 1번
-> 표로 나타내면
|숫자|0|1|2|3|4|5|
|개수|3|1|3|2|2|1|
-> 누적합으로 바꾸면
|각숫자|0|1|2|3| 4| 5|
|누적합|3|4|7|9|11|12|
-> 이를 통해 인덱스를 얻을 수 있음
0은 0~2 인덱스
1은 3 인덱스
2는 4~6 인덱스
3은 7~8 인덱스
4는 9~10 인덱스
5는 11 인덱스
-> 각 숫자를 인덱스에 따라 배열에 넣어주면
0, 0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5
```

```c
#include <stdio.h>
#include <stdlib.h>

const int n = 7;

void countingSort(int arr[]){
    int *cntArr;
    int max = arr[0];
    for(int i=1; i<n; i++) max = max>arr[i]?max:arr[i]; //리스트에서 최대값 추출
    cntArr = (int*)malloc(sizeof(int) * (max + 1)); //카운팅 배열 할당
    for(int i=0; i<=max; i++) cntArr[i] = 0; //카운팅 배열 초기화
    for(int i=0; i<n; i++){ //카운팅 시작
        cntArr[ arr[i] ] ++;
    }
    for(int i=1; i<=max; i++){ //누적 합 계산
        cntArr[i] = cntArr[i] + cntArr[i-1];
    }
    int tmp[n]; for(int i=0; i<n; i++) tmp[i] = arr[i]; //원본 데이터
    for(int i=n-1; i>=0; i--){ //뒤 부터 탐색
        arr[ cntArr[ tmp[i] ] - 1 ] = tmp[i]; //인덱스가 0부터 시작하므로,
                                      //cntArr[tmp[i]]-1 을 인덱스로 한다
        cntArr[ tmp[i] ]--;
    }
}

int main(){
    int arr[n] = {3, 0, 1, 1, 2, 2, 1};
    countingSort(arr);
    for(int i=0; i<n; i++) printf("%d ", arr[i]);
}
```

```python
def counting_sort(arr):
	cntArr = [0 for _ in range(max(arr)+1)]

	for i in range(len(arr)):
		cntArr[arr[i]] += 1

	for i in range(1,max(arr)+1):
		cntArr[i] = cntArr[i] + cntArr[i-1]

	tmp = arr[:]
	for i in range(len(arr)-1,-1,-1):
		arr[cntArr[tmp[i]]-1] = tmp[i]
		cntArr[tmp[i]] -= 1

arr = [3, 0, 1, 1, 2, 2, 1]
counting_sort(arr)
print(arr)
```
