# 이진 탐색 ( Binary Search )

- 순차 탐색은 배열의 길이가 n이라면, 최악의 경우 $O(N)$ 의 시간이 걸림
- 이진 탐색은 탐색을 할 때, 탐색 범위를 1/2 씩 줄여나가며 탐색하는 방법
- **데이터가 정렬 되어 있을 때**만 사용가능

## 동작 과정

- 데이터의 중앙값 선택
- 선택한 값과 찾고자 하는 값을 비교
- 비교결과를 통해 탐색범위 변경
  - 선택한 값이 더 작다면, 탐색 범위의 끝을 중앙-1로 변경하여 탐색범위를 왼쪽 반으로 줄임
  - 선택한 값이 더 크다면, 탐색 범위의 시작을 중앙+1로 변경하여 탐색범위를 오른쪽 반으로 줄임
  - 같다면, 종료
- 찾을 때까지 위 과정을 반복

- **시간복잡도 :** $O(log_2N)$

## 구현

```c
#include <stdio.h>
#define N 10

int main(){
    int arr[N]={2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int front=0, rear=N-1, mid, find;
    scanf("%d", &find);
    while(front<=rear){
        mid=(front+rear)/2;
        if(arr[mid]==find){
            printf("arr[%d]", mid);
            return 0;
        }
        if(arr[mid]<find){
            front=mid+1;
        }
        if(find<arr[mid]){
            rear=mid-1;
        }
    }
    printf("Not Exist");
}
```

```c
#include <stdio.h>
int binary_search(int arr[],int start,int end,int find){
		if(start>end){
				printf("Not Exist");
				return -1;
		}
		int mid = (start+end)/2;
		if(arr[mid]==find){
				printf("arr[%d]", mid);
        return 0;
		}
		if(arr[mid]<find){
				return binary_search(arr,mid+1,end,find);
    }
    if(find<arr[mid]){
        return binary_search(arr,start,mid-1,find);
    }
}

int main(){
    int arr[N]={2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
		int x = 6
		binary_search(arr,0,N,x);
}
```

```python
def binary_search(arr,start,end,find):
	if start > end:
		print("Not exist")
		return -1
	mid = (start+end)//2
	if arr[mid] == find:
		print("arr[%d]"%(mid))
		return
	if arr[mid] < find:
		return binary_search(arr,mid+1,end,find)
	if arr[mid] > find:
		return binary_search(arr,start,mid-1,find)

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 6
binary_search(arr,0,len(arr),x)
```

### 참고할 라이브러리

- cpp : binary search, lower bound, upper bound
  - [https://www.geeksforgeeks.org/binary-search-functions-in-c-stl-binary_search-lower_bound-and-upper_bound/](https://www.geeksforgeeks.org/binary-search-functions-in-c-stl-binary_search-lower_bound-and-upper_bound/)
- python : bisect
  - [https://docs.python.org/3/library/bisect.html](https://docs.python.org/3/library/bisect.html)
