def digits(base):
    res = []
    for i in range(2,base):
        if (base-1)%i == 0:
            res.append(i)
    return res