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
		