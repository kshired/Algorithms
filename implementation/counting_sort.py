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