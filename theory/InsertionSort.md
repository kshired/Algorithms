# Insertion Sort

Insertion Sort는 모든 자료를 앞에서부터 차례로 **이미 정렬 된 부분**과 비교하여 적절한 위치에 삽입하는 방식으로 정렬을 함.

```
"31" 25 12 22 11    첫번째 원소인 31을 적절한 위치에 넣는다.
31 "25" 12 22 11    두번째 원소인 25를 적절한 위치에 넣는다.
25 31 "12" 22 11    세번째 원소인 12를 적절한 위치에 넣는다.
12 25 31 "22" 11    네번째 원소인 22를 적절한 위치에 넣는다.
12 22 25 31 "11"    다섯번째 원소 11을 적절한 위치에 넣는다.
```

최선 : 이미 정렬 되어 있는 경우, 두번째 for문이 돌지 않음. 따라서 바깥 for문만 돌기 때문에, $O(n)$.

최악 : 역순으로 정렬 되어 있는 경우, $\frac{n(n-1)}{2}$ 이기 때문에 $O(n^2)$.

```c
void insertion_sort(int arr[], int size){
	for(int i=0;i<size-1;++i){
		int cur = arr[i+1];
		for(int j=i;j>=0;--j){
			if(arr[j] > cur) arr[j+1] = arr[j];
			else break;
		}
		arr[j+1] = cur;
	}
}
```

```python
def insertion_sort(arr):
	for i in range(len(arr)-1):
		cur = arr[i+1]
		for j in range(i,-1,-1):
			if arr[j] > cur:
				arr[j+1] = arr[j]
			else:
				break
		arr[j+1] = cur
```
