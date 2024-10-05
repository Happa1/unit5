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
class Stack():
    def __init__(self):
        self.data=Queue()

    def push(self,value):
        self.data.enque(value)

    def pop(self):
        temp=Queue()
        while not self.data.isEmpty():
            item=self.data.deque()
            if self.data.isEmpty():
                self.data=temp
                return item
            else:
                temp.enque(item)

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False