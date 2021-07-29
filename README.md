# 꾸준히 알고리즘 문제 풀기

[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=python4)](https://solved.ac/python4)

## 이론

### Search

- [Linear Search](./theory/LinearSearch.md)
- [Binary Search](./theory/BinarySearch.md)

### Data Structures

- [Stack](./theory/Stack.md)
- [Queue](./theory/Queue.md)
- [Deque](./theory/Deque.md)
- [Heap](./theory/Heap.md)
- [Tree](./theory/Tree.md)
- [Binary Tree](./theory/BinaryTree.md)
- [Binary Search Tree](./theory/BinarySearchTree.md)
- [Union Find](./theory/UnionFind.md)
- [Segment Tree](./theory/SegmentTree.md)

## 기록

알고리즘 문제를 푼 날짜와, 푼 문제를 정리합니다.

- 2021.05.04 : baekjoon 1012, 1260, 1987, 2178, 2606, 2667, 10026, 11724

- 2021.05.05 : baekjoon 1516, 1766, 2252, 2623

- 2021.05.07 : baekjoon 1065, 1316, 1654, 2805, 2941, 4344, 4673, 5622, 9012, 15596

- 2021.05.08 : baekjoon 1037, 1436, 1504, 1753, 1916, 7568, 10870, 10872, 11779

- 2021.05.09 : baekjoon 1712, 2263, 10815, 10816, 11728 && leetcode 6, 8, 22

- 2021.05.10 : baekjoon 1717, 3078, 8279, 10811, 11003 && leetcode 3, 130

- 2021.05.11 : baekjoon 1449, 1463, 1699, 1931, 2294, 4796, 9465, 11000, 11047, 11055, 11726, 11727, 13904, 17509 && programmers 네트워크, 단어변환, 여행경로, 타겟넘버

- 2021.05.12 : baekjoon 1005, 1520, 1966, 2133, 2631, 10972, 11051, 11054, 11722

- 2021.05.13 : baekjoon 1167, 1181, 2075, 5582, 9251,9252, 9663, 10814, 10845, 10866, 11866, 14888, 15649 ~ 15652, 16562, 20299 ~ 20303

- 2021.05.14 : baekjoon 1918, 1967, 1991

- 2021.05.15 : baekjoon 1269, 1351, 2287, 10971, 11659, 11660, 11689, 16496

- 2021.05.16 : baekjoon 2042, 2960 && programmers 다단계 칫솔 판매, 로또의 최고 순위와 최저 순위, 행렬 테두리 회전하기

- 2021.05.17 : baekjoon 1197, 1354, 1613, 1676, 1764, 2225, 5430, 10159,11279, 12286, 11404, 11505, 13398

- 2021.05.18 : baekjoon 1915, 1958, 2812, 4195, 11333, 17298

- 2021.05.19 : baekjoon 1202, 1647, 1697, 2468, 2573, 2583, 2644, 4963, 7569, 7576, 9466, 11725, 14002, 14003, 14502

- 2021.05.20 : baekjoon 1365, 1818, 2352, 2493, 2550, 3745, 7662, 12014, 13711

- 2021.05.21 : baekjoon 1655 && leetcode 11, 17, 29, 31, 38, 50, 200

- 2021.05.22 : baekjoon 2162, 10423, 12781 && leetcode 34

- 2021.05.23 : baekjoon 2473 && leetcode 64, 102

- 2021.05.24 : baekjoon 2662, 4781, 7579, 14728

- 2021.05.25 : baekjoon 1208, 2143, 2166, 2568, 11758, 12852, 17387

- 2021.05.26 : baekjoon 9527 && leetcode 53

- 2021.05.27 : baekjoon 1043, 1976

- 2021.05.28 : baekjoon 1922, 2887, 4386, 6497, 14621, 16202

- 2021.05.29 : baekjoon 1253, 1708

- 2021.05.30 : baekjoon 1715

- 2021.05.31 : leetcode 75

- 2021.06.05 : leetcode 43, 70

- 2021.06.09 : leetcode 46, 104, 121, 146

- 2021.06.10 : baekjoon 21866, 21867, 21868, 21869

- 2021.06.12 : baekjoon 1389, 1926, 2096, 7562

- 2021.06.13 : baekjoon 1240, 2479 && programmers 주식가격, H-Index

- 2021.06.14 : baekjoon 1103, 1405

- 2021.06.16 : baekjoon 13604, 15591

- 2021.06.18 : baekjoon 2206, 9019

- 2021.06.19 : baekjoon 1744, 5014

- 2021.06.21 : baekjoon 1238, 15686

- 2021.06.22 : baekjoon 1759, 17836

- 2021.06.23 : baekjoon 1937, 10942

- 2021.06.24 : baekjoon 1325, 5639

- 2021.06.26 : baekjoon 1182, 1427, 1543

- 2021.07.04 : baekjoon 1026, 9656

- 2021.07.06 : baekjoon 9095, 11049

- 2021.07.29 : programmers 메뉴 리뉴얼, 합승 택시 요금,

## makecode.py

### What is this?

백준 문제 번호를 입력하면, ps용 파이썬 코드의 기본 틀을 만들어주는 간단한 프로그램입니다.
일괄적으로 만들어주면 좋겠다 싶어서, 만들었습니다.

**생성 코드 예시**

```python
# https://acmicpc.net/problem/9656
# 돌 게임 2

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())
```

### How to use?

- `python3 makecode.py 문제 번호`
- `python3 makecode.py` 후, 문제 번호 입력

### Dependencies

```
requests
```
