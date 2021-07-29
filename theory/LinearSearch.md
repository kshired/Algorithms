# 순차 탐색 ( Sequential Search )

- 배열(리스트 혹은 데이터의 집합)의 처음부터 끝까지 순서대로 탐색하는 방법
- 효율이 좋지는 않지만, 구현이 간단하여 간단한 데이터를 다룰 때 자주 사용

구현

```c
#include <stdio.h>
void linear_search(int arr[],int size,int x){
		for(int i=0; i<size; i++){
        if(arr[i] == x){
            printf("[[find]] index : %d\n", i);
            break;
        }
    }
}
int main(){
    const int n = 10;
    int arr[n] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    int x =  6;
    linear_search(arr,n,x);
}
```

```python
def linear_search(arr,x):
	for i in range(len(arr)):
		if arr[i] == x:
			print("[[find]] index :",i)
			break

arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
x = 6
linear_search(arr,x)
```

### 자기 구성 순차 탐색 ( Self-Organizing Sequential Search )

- 자주 사용되는 항목을 배열의 앞쪽에 배치해서 순차탐색의 계산량을 줄여주는 방법
- 전진 이동법과 전위법 등이 있다.

**전진 이동법(Move to Front Method)**

- 어떤 항목이 탐색이 되면 그 항목을 배열의 맨 앞에 배치하는 방법
- 한 번 찾은 데이터를 계속해서 찾을 경우 탐색의 효율이 올라감

구현

```c
#include <stdio.h>
int Move2Front(int arr[], int n, int x){
    for(int i=0; i<n; i++){
        if(arr[i] == x){
            for(int j=i-1; j>=0; j--){
                arr[j+1] = arr[j];
            }
            arr[0] = x;
            return i;
        }
    }
    return -1;
}

int main(){
    const int n = 10;
    int arr[n] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    int x =  6;
    int result = Move2Front(arr, n, x);
    if(result == -1) printf("Not Found\n");
    else{
        printf("[[find]] idx = %d\n", result);
        printf("arr = {");
        for(int i=0; i<n; i++) printf("%d ", arr[i]); printf("}\n");
    }
}
```

```python
def move_to_front(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            for j in range(i-1,-1,-1):
                arr[j+1] = arr[j]
                arr[0] = x
            return i
    return False

arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
x = 6
res = move_to_front(arr,x)
if not res:
    print("Not found")
else:
    print("[[find]] index :",res)
    print("arr:",arr)
```

**전위법(Transpose Method)**

- 발견 될 때 마다 한 칸씩 앞으로 이동시키는 방법
- 전진 이동법은 최근에 찾은 것이 앞으로 간다면, 전위법은 자주 나온 것이 앞으로 감

구현

```c
#include <stdio.h>
int transpose(int arr[], int n, int x){
    for(int i=0; i<n; i++){
        if(arr[i] == x) {
            if (i != 0) {
                int tmp = arr[i];
                arr[i] = arr[i - 1];
                arr[i - 1] = tmp;
            }
            return i;
        }
    }
    return -1;
}

int main(){
    const int n = 10;
    int arr[n] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    int x =  6;
    int result = transpose(arr, n, x);
    if(result == -1) printf("Not Found\n");
    else{
        printf("[[find]] idx = %d\n", result);
        printf("arr = {");
        for(int i=0; i<n; i++) printf("%d ", arr[i]); printf("}\n");
    }
}
```

```python
def transpose(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            if i!=0 :
                arr[i],arr[i-1] = arr[i-1],arr[i]
            return i
    return False

arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
x = 6
res = transpose(arr,x)
if not res:
    print("Not found")
else:
    print("[[find]] index :",res)
    print("arr:",arr)
```
