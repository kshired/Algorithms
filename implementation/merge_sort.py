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

	