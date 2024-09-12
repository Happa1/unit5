# Quiz078
![quiz_078.jpg](..%2FImage%2Fqustion%2Fquiz_078.jpg)
**Fig1. Quiz 078**

![quiz_078.jpeg](..%2FImage%2Fnote%2Fquiz_078.jpeg)
**Fig2. Note Quiz 078**

## 1.solution
```.py
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
```

## 2.proof of work
![quiz_078.png](..%2FImage%2Fevidence%2Fquiz_078.png)
**Fig3. test of quiz 078**
