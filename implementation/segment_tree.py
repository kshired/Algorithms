'''
init(arr: List, tree: List, node: int, start: int, end: int) -> int 

arr : 배열
tree : 세그먼트 트리
node의 관할 영역 : [start,end]
'''
def init(arr, tree, node, start, end):
    if start == end: # 리프 노드인 경우
        tree[node] = arr[start]
        return tree[node]
    tree[node] = init(arr, tree, node*2, start,(start+end)//2) + init(arr, tree, node*2+1, (start+end)//2+1, end)
    return tree[node] # 리프 노드가 아니면 자식들의 합을 저장
    
'''
sum(arr: List, tree: List, node: int, start: int, end: int, left: int, right: int) -> int 

arr : 배열
tree : 세그먼트 트리
node의 관할 영역 : [start,end]
구하자고 하는 영역: [left, right]
'''
def sum(arr, tree, node, start, end, left, right):
    if left > end or right < start: # 겹치는 구간이 없는 경우
        return 0

    if left <= start and end <= right: # [left, right]가 [start, end]를 완전히 포함하는 경우
        return tree[node]

    return sum(arr, tree, node*2, start, (start+end)//2, left, right) + sum(arr, tree, node*2+1, (start+end)//2+1, end, left, right)
	    # [start, end]가 [left, right]를 완전히 포함하거나
	    # 두 구간이 겹쳐 있는 경우
		# 왼쪽 서브 트리와 오른쪽 서브 트리에서 다시 탐색 시작
'''
update(arr: List, tree: List, node: int, start: int, end: int, idx: int, diff: int) -> None

arr : 배열
tree : 세그먼트 트리
node의 관할 영역 : [start,end]
구하자고 하는 영역: [left, right]
idx: 바꾸자고 하는 위치
diff: 변하는 정도
'''

def update(arr, tree, node, start, end, idx, diff):
    if idx < start or idx > end: # 범위를 벗어남
        return
    tree[node] += diff # 범위에 포함되면 diff를 더해줌.
    if start != end: # 리프 노드가 아니면, 왼쪽 서브트리와 오른쪽 서브트리 모두 update
        update(arr, tree, node*2, start, (start+end)//2, idx, diff)
        update(arr, tree, node*2+1, (start+end)//2+1, end, idx, diff)
        