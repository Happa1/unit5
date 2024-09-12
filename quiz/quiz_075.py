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

def get_k(n): # get the k
    k=0
    while 2**k<n+k+1:
        k+=1
    return k

test=get_k(4)
print(test)