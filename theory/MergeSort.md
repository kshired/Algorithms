# Merge Sort

합병 정렬 ( merge sort )도 퀵 정렬( quick sort )와 같이 divide and conquer 방법을 사용함

**작동방식**

1. 길이가 0 또는 1인 리스트는 정렬 된 것으로 본다
2. 정렬 되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분의 리스트로 나눈다.
3. 각 부분 리스트를 재귀적으로 합병정렬을 이용해 정렬한다
4. 두 부분 리스트를 다시 하나의 정렬 된 리스트로 합병한다.

```cpp
#include <cstdio>
#include <cstdlib>

const int n = 8;

void merge(int arr[], int left[], int right[], int size) {
  int j = size / 2;
  int k = size - (size / 2);
  int p, q, i;
  p = q = i = 0;

  while (p < j && q < k) {
    if (left[p] < right[q]) {
      arr[i++] = left[p++];
    } else {
      arr[i++] = right[q++];
    }
  }

  while (p < j) {
    arr[i++] = left[p++];
  }

  while (q < k) {
    arr[i++] = right[q++];
  }
}

void mergeSort(int arr[], int size) {
  if (size <= 1) {
    return;
  }
  int *left = (int *)malloc(sizeof(int) * (size / 2));
  int *right = (int *)malloc(sizeof(int) * (size - (size / 2)));
  for (int i = 0; i < (size / 2); ++i) {
    left[i] = arr[i];
  }
  for (int i = 0; i < (size - (size / 2)); ++i) {
    right[i] = arr[i + (size) / 2];
  }

  mergeSort(left, size / 2);
  mergeSort(right, size - (size / 2));
  merge(arr, left, right, size);
  free(left);
  free(right);
}

int main() {
  int arr[n] = {1, 3, 5, 7, 2, 4, 6, 8};
  mergeSort(arr, n);
  for (int i = 0; i < n; i++) printf("%d ", arr[i]);
  printf("\n");
}
```

```cpp
#include <cstdio>

const int n = 8;

void merge(int arr[], int left, int mid, int right) {
  int i = left, j = mid + 1, k = left;
  int tmp[n] = {0};
  while (i <= mid || j <= right) {
    if (i > mid)
      tmp[k++] = arr[j++];
    else if (j > right)
      tmp[k++] = arr[i++];
    else if (arr[i] <= arr[j])
      tmp[k++] = arr[i++];
    else
      tmp[k++] = arr[j++];
  }
  for (int i = left; i <= right; ++i) {
    arr[i] = tmp[i];
  }
}

void mergeSort(int arr[], int left, int right) {
  if (left < right) {
    int mid = (left + right) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
  }
}

int main() {
  int arr[n] = {1, 3, 5, 7, 2, 4, 6, 8};
  mergeSort(arr, 0, n - 1);
  for (int i = 0; i < n; i++) printf("%d ", arr[i]);
}
```

```python
n = 8
def merge(arr, left, mid, right):
	i = left
	j = mid + 1
	k = left
	tmp = [0 for _ in range(n)]
	while i <= mid or j <= right:
		if i > mid:
			tmp[k] = arr[j]
			k += 1
			j += 1
		elif j > right:
			tmp[k] = arr[i]
			k += 1
			i += 1
		elif arr[i] <= arr[j]:
			tmp[k] = arr[i]
			k += 1
			i += 1
		else:
			tmp[k] = arr[j]
			k += 1
			j += 1

	for i in range(left,right+1):
		arr[i] = tmp[i]

def merge_sort(arr, left, right):
	if left < right:
		mid = (left + right)//2
		merge_sort(arr, left, mid)
		merge_sort(arr, mid + 1, right)
		merge(arr, left, mid, right)

arr = [1, 3, 5, 7, 2, 4, 6, 8]
merge_sort(arr, 0, n-1)
print(arr)

```
