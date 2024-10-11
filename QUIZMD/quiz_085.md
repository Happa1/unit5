# Quiz085
![quiz_085.jpg](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_085.jpg)
**Fig1. Quiz 085**

![quiz_085.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_085.jpeg)
**Fig2. Note Quiz 085**

## 1.solution
```.py
from quiz_087 import Queue
def FUNC(input):
    queue=Queue()
    l=len(input)
    n=1
    for i in range(7):
        count = 0
        for j in range(l):
            if input[j]==n:
                count+=1
        queue.enque(count)
        n+=1

    list=[]
    while not queue.isEmpty():
        list.append(queue.deque())
    return list

test=FUNC(input=[3,7,7,7,5,5,1])
print(test)

```

## 2.proof of work
![quiz_085.png](..%2FImage%2Fevidence%2Fquiz_081-088%2Fquiz_085.png)
**Fig3. test of quiz 085**
