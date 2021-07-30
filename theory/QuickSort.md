# Quick Sort

Quick Sort는 divide and conquer를 사용하는 정렬 알고리즘이다.

**작동 방식**

1. 리스트에서 하나의 원소를 선택하고, 그 원소를 피봇으로 지정.
2. 피봇보다 작은 원소들은 모두 피봇의 왼쪽으로, 더 큰 원소들은 모두 피봇의 오른쪽으로 이동.
3. 피봇을 기준으로 분할 된 두 개의 작은 리스트에 대해 리스트의 크기가 0또는 1이 될 때까지 재귀적으로 1, 2 과정을 반복.

**직접 구현한 퀵소트**

```cpp
void quickSort(int arr[], int size) {
  if (size <= 1) {
    return;
  }

  int pivot = arr[size / 2];

  int *left = (int *)malloc(sizeof(int) * size);
  int *right = (int *)malloc(sizeof(int) * size);
  int j = 0;
  int k = 0;

  for (int i = 0; i < size; ++i) {
    if (i == (size) / 2) {
      continue;
    }
    if (pivot <= arr[i]) {
      left[j++] = arr[i];
    } else if (pivot > arr[i]) {
      right[k++] = arr[i];
    }
  }

  quickSort(left, j);
  quickSort(right, k);

  for (int i = 0; i < j; ++i) {
    arr[i] = left[i];
  }

  arr[j] = pivot;

  for (int i = j + 1; i < size; ++i) {
    arr[i] = right[i - j - 1];
  }

  free(left);
  free(right);
}
```

그냥 swap처리하고 이러면, 귀찮고해서 left, right를 담는 메모리를 allocation해줘서 분할 정복 해버렸다.

하지만, 이렇게하면 메모리가 너무 많이 사용되니 아래와 같은 방법을 사용하자.

**예시**

1. pivot보다 큰 값을 pivot보다 왼쪽에서 찾고(큰 값이 나타날 때 까지 i 를 증가시킵니다.)
2. pivot보다 작은 값을 pivot보다 오른쪽에서 찾습니다.(작은 값이 나타날 때 까지 j를 감소시킵니다.)
3. pivot을 기준으로 값 비교가 완료되었다면, i와 j 인덱스를 비교합니다.
4. i <= j이면 두 값을 교환합니다.
5. i <= j이면 계속 4번 항목을 반복합니다.6. 5번 항목이 끝났다면, 피벗 왼쪽 부분과 오른쪽 부분에 대해 각각 재귀 호출 합니다.

```cpp
void quickSort(int arr[], int left, int right) {
    int i = left, j = right;
    int pivot = arr[(left + right) / 2];
    int temp;
    do {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i<= j) {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    } while (i<= j);

    /* recursion */
    if (left < j)
        quickSort(arr, left, j);

    if (i < right)
        quickSort(arr, i, right);
}
```

```python
def quick_sort(arr, left, right):
	i = left
	j = right
	pivot = arr[(left+right)//2]

	while True:
		while arr[i] < pivot:
			i += 1
		while arr[j] > pivot:
			j -= 1
		if i <= j:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1
		if i > j:
			break

	if left < j:
		quick_sort(arr, left, j)
	if i < right:
		quick_sort(arr, i, right)

arr = [5, 4, 3, 2, 1]
quick_sort(arr, 0, 4)
```
