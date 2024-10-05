from quiz_087 import Queue
def FUNC(input):
    queue=Queue()
    l=len(input)
    n=1
    for i in range(7):
        for j in range(l):
            count=0
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
