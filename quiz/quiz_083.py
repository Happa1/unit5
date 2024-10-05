def FUNC(N):
    if len(N) == 1:
        return N[0]
    else:
        mid = len(N) // 2
        L = FUNC(N[:mid])
        R = FUNC(N[mid:])
    return L + R

test=FUNC(N=[5,3,1,10])
print(test)