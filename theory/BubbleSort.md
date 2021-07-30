# Bubble Sort

- 버블 정렬은 인접한 두 원소를 비교해 정렬
- 가장 기초적이지만, 시간 복잡도가 $O(n^2)$ 이므로 자주 사용하지는 않음.

```
"55 07" 78 12 42 -> swap
07 "55 78" 12 42
07 55 "78 12" 42 -> swap
07 55 12 "78 42" -> swap
"07 55" 12 42 78
07 "55 12" 42 78 -> swap
07 12 "55 42" 78 -> swap
"07 12" 42 55 78
07 "12 42" 55 78
"07 12" 42 55 78
"07 12 42 55 78"  정렬 끝
```

ex)

```c
for(int i=0; i<n; i++){
    for(int j=0; j<n-1; j++){
        if(arr[j] > arr[j+1]){
            int tmp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = tmp;
        }
    }
}
```

- 버블 정렬은 정렬 도중 완전히 정렬 되었음에도 불구하고 끝까지 연산을 하는 경우가 존재하기에, 그 비효율을 막기위해 flag를 사용하여 cut
- 바깥 for문 내부에 flag를 1로 초기화해주고, 안쪽 for문 내에서 swap이 일어나는 경우 flag를 0으로 바꿔 줌. 만약 안쪽 for문이 끝났음에도, flag가 1이면 정렬이 끝났다는 것이니 break하여 cut

```c
for(int i=0; i<n; i++){
    int flag = 1;
    for(int j=0; j<n-1; j++){
        if(arr[j] > arr[j+1]){
            flag = 0;
            int tmp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = tmp;
        }
    }
    if(flag) break;
}
```
