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
def get_msg(msg:str):
    k=get_k(msg=msg)
    position=get_ham_position(k=k)
    m_count=0
    total_msg=[]
    for i in range(len(msg)+k):
        total_msg.append(-1) #create the length of message

        if i not in position:
            total_msg[i]=msg[m_count] # add message letter to its position
            m_count+=1

    return total_msg

test=get_msg(msg='1011')
print(test)