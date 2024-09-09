def get_k(msg:str): # get the k
    n=len(msg)
    k=0
    while 2**k<n+k+1:
        k+=1
    return k

def get_ham_position(k):
    output=[]
    for i in range(k):
        output.append(2**i-1)
    return output

def get_check_p(len_msg,p):
    output=[]
    for i in range(len_msg+1):
        n = i & (2 ** p)
        if n:
            output.append(i-1)
    return output

def final_msg(msg:str):
    k=get_k(msg)
    print(f"k number is {k}")
    position=get_ham_position(k=k)
    print(f"The position of parity bits are {position}")

    m_count=0
    total_msg=[]
    for i in range(len(msg)+k):
        total_msg.append(-1) #create the length of message

        if i not in position:
            total_msg[i]=msg[m_count] # add message letter to its position
            m_count+=1
    print(f"This is the total message {total_msg}")

    pr = 0
    for j in range(len(msg) + k):
        if j in position: # if it is parity bits position
            check_p=get_check_p(len(msg)+k,pr)
            print(f"These are positions that you need to check{check_p}")
            b_sum=0
            for p in check_p: # loop p in the position that we need to check
                b_sum += int(total_msg[p])
            b_sum = b_sum+1
            if b_sum%2==0:
                total_msg[j]=0
            else:
                total_msg[j]=1
            pr+=1

    return total_msg



test=final_msg('1011')
print(test)