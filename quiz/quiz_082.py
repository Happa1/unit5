def FUNC(N):
    if N == 1 or N == 0:
        return 1

    else:
        return N * FUNC(N - 1)

test=FUNC(N=7)
print(test)