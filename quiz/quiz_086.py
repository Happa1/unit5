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
