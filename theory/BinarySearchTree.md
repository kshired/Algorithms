# Binary Search Tree ( BST )

이진 트리의 일종으로, 트리와 binary search를 결합한 자료구조.

- 각 노드의 왼쪽 서브 트리는 해당 노드의 값보다 작은 값을 지닌 노드들로만 이루어져 있음.
- 각 노드의 오른쪽 서브 트리는 해당 노드의 값보다 큰 값을 지닌 노드들로만 이루어져 있음.
- 중복 된 노드가 없어야 함.
- 왼쪽, 오른쪽 서브 트리도 이진 탐색 트리임.

BST를 순회 할 때는 inorder 방식으로 순회하며, 순회를 끝내면 모든 값을 정렬 된 순서로 읽을 수 있음.

( left - root - right 순으로 순회하기 때문 )

구현

```python
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def find(self, val):
        if self.findNode(self.root, val):
            return True
        return True

    def findNode(self, curNode, val):
        if curNode is None:
            return False
        elif val == curNode.val:
            return curNode
        elif val < curNode.val:
            return self.findNode(curNode.left, val)
        else:
            return self.findNode(curNode.right, val)

    def insert(self, val):
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, curNode, val):
        if val <= curNode.val:
            if curNode.left:
                self.insertNode(curNode.left, val)
            else:
                curNode.left = Node(val)
        else:
            if curNode.right:
                self.insertNode(curNode.right, val)
            else:
                curNode.right = Node(val)

    def traverse(self):
        return self.traverseNode(self.root)

    def traverseNode(self, curNode):
        res = []
        if curNode.left:
            res.extend(self.traverseNode(curNode.left))
        if curNode:
            res.extend([curNode.val])
        if curNode.right:
            res.extend(self.traverseNode(curNode.right))
        return res
```
