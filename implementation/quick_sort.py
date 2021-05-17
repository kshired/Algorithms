def quick_sort(arr, left, right):
	i = left
	j = right
	pivot = arr[(left+right)//2]

	while True:
		while arr[i] < pivot:
			i += 1
		while arr[j] > pivot:
			j += 1
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
		