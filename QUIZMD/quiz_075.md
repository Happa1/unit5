# Quiz075
![quiz_075.jpg](..%2FImage%2Fqustion%2Fquiz_075.jpg)
**Fig1. Quiz 075**

![quiz_075.jpeg](..%2FImage%2Fnote%2Fquiz_075.jpeg)
**Fig2. Note Quiz 075**

## 1-a.solution SL
```.py
def get_k(msg:str): # get the k
    n=len(msg)
    k=0
    while 2**k<n+k+1:
        k+=1
    return k
```

## 1-b.solution HL
```.py
def get_k(msg:str): # get the k
    n=len(msg)
    k=0
    while 2**k<n+k+1:
        k+=1
    return k

import matplotlib.pyplot as plt

x_list=[]
y_list=[]
k=0

print_true=True

for i in range(1,1000):
    n=i
    while 2**k<n+k+1:
        k+=1
    x_list.append(n)
    y_list.append(n/(k+n)*100)
    if y_list[-1]>=90 and print_true==True:
        print_true=False
        print(f'when the length of the message is {n}, the efficiency gets bigger than 90%')

plt.plot(x_list, y_list)
plt.show()
```

## 2.proof of work
![quiz_075.png](..%2FImage%2Fevidence%2Fquiz_075.png)
**Fig3. test of quiz 075**


