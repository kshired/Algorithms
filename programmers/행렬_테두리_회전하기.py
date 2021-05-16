def solution(rows, columns, queries):
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    
    val = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = val
            val += 1
    
    res = []
    
    for query in queries:
        x1,y1,x2,y2 = query
        
        tmp = arr[x1-1][y2-1]
        minimum = min(tmp,min(arr[x1-1][y1-1:y2-1]))
        arr[x1-1][y1:y2] = arr[x1-1][y1-1:y2-1]
        

        for i in range(x1,x2):
            minimum = min(minimum,arr[i][y1-1])
            arr[i-1][y1-1] = arr[i][y1-1]

        minimum = min(minimum, min(arr[x2-1][y1:y2]))
        arr[x2-1][y1-1:y2-1] = arr[x2-1][y1:y2]

        for i in range(x2-2, x1-2, -1):
            minimum = min(minimum,arr[i][y2-1])
            arr[i+1][y2-1] = arr[i][y2-1]

        arr[x1][y2-1] = tmp
        
        res.append(minimum)
    return res