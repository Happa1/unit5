def get_check_p(len_msg,p):
    output=[]
    for i in range(len_msg+1):
        n = i & (2 ** p)
        if n:
            output.append(i-1)
    return output

test=get_check_p(7,0)
print(test)