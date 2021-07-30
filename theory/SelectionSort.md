# Selection Sort

selection sort는 최소 값을 선택하여 맨 앞으로 옮겨주는 방식으로 정렬을 함

```
/ 2 5 3 "1" 4 7 6
1/ 5 3 "2" 4 7 6
1 2 3/ 5 "4" 7 6
1 2 3 4 5/ 7 "6"
1 2 3 4 5 6 7 /
```

최소 값의 index를 저장하여, 현재 데이터와 index에 있는 데이터를 swap하여 정렬.

첫 for문은 1~n, 두번 째 for문은 ( n-1, n-2, ..., 1 ) 따라서, $\frac{n(n-1)}{2}$ 이므로, $O(n^2)$ 의 시간복잡도를 가짐.

```c
int selection_sort(int arr[], int size){
	for(int i=0;i<size;++i){
		int min_idx = i;
		for(int j=i+1;j<size;++j){
			if(arr[min_idx]>arr[j]){
				min_idx = j;
			}
		}
		int tmp = arr[i];
		arr[i] = arr[min_idx];
		arr[min_idx] = tmp;
	}
}
```

```python
def selection_sort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1,len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
```
