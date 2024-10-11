# Quiz086
![quiz_086.jpg](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_086.jpg)
**Fig1. Quiz 086**

![quiz_086.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_086.jpeg)
**Fig2. Note Quiz 086**

## 1.solution
```.py
class container:
    def __init__(self):
        self.data=[None]
    def get(self):
        return self.data[0]

    def set(self, x):
        self.data[0]=x

class Queue:
    def __init__(self):
        self.queue=[]

    def enque(self, item):
        self.item=item
        c=container()
        c.set(self.item)
        self.queue.append(c)
        return self.queue

    def deque(self):
        if self.isEmpty()==False:
            out=self.queue[0].get()
            self.queue=self.queue[1:]
            return out
        else:
            return None

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False

q = Queue()

q.enque(1)
q.enque(2)
q.enque(3)


print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())

```

## 2.proof of work
![quiz_086.png](..%2FImage%2Fevidence%2Fquiz_081-088%2Fquiz_086.png)
**Fig3. test of quiz 086**
