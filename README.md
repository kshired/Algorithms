# kshired.Algorithms

[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=python4)](https://solved.ac/python4)

## [이론](markdowns/Theory.md)

- 문제를 풀면서 공부했던 이론들을 정리한 마크다운 문서입니다.

## [기록](markdowns/Record.md)

- 알고리즘 문제를 푼 날짜와, 푼 문제를 정리합니다.

## [makecode.py](./makecode.py)

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
