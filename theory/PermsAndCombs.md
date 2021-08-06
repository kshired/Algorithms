# Permutations and Combinations

Python collections의 itertools를 사용하지 않고 combinations와 permutations를 구현하는 방법.

```python
def combinations(arr,n):
    if n == 0:
        return [[]]
    res = []

    for i in range(len(arr)):
        now = arr[i]
        rest = arr[i+1:]
        for combination in combinations(n-1):
            res.append([now]+combination)
    return res
```

```python
def permuations(arr,n)
    if n == 0:
      return [[]]

    res = []

    for idx, now in enumerate(arr):
        for permutation in permutations(arr[:i]+arr[i+1:],n-1):
            res += [[now]+p]

    return res
```
