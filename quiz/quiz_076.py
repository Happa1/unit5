def get_ham_position(k):
    output=[]
    for i in range(k):
        output.append(2**i-1)
    return output

test=get_ham_position(k=3)
print(test)
