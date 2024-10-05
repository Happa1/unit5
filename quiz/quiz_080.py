def FUNC(N):
    if len(N) == 1:
        return N[0]

    M = FUNC(N[1:])

    if N[0] > M:
        return N[0]
    else:
        return M

test=FUNC(N=[3,5,8,7])
print(test)
