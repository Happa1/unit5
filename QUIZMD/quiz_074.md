# Quiz074
![quiz_074.jpg](..%2FImage%2Fqustion%2Fquiz_074.jpg)
**Fig1. Quiz 074**

![quiz_074.jpeg](..%2FImage%2Fnote%2Fquiz_074.jpeg)
**Fig2. Note Quiz 074**

## 1.solution
```.py
def build_packet():
    n=input("Enter the message")
    return n

def check_error(packet):
    correct_msg=""
    if len(packet)%3!=0:
        correct_msg="Message cannot be divided by 3"

    else:
        len_data=len(packet)//3
        msg=packet[0:len_data]
        copy_1=packet[len_data:len_data*2]
        copy_2=packet[len_data*2:len_data*3]
        if msg!=copy_1:
            if msg!=copy_2 and copy_1==copy_2:
                correct_msg=copy_1
            elif msg!=copy_2 and copy_1!=copy_2:
                correct_msg="Incorrect msg"
        else:
            correct_msg=msg
    return correct_msg

test=check_error(packet=build_packet())
print(test)
```

## 2.proof of work
![quiz_074.png](..%2FImage%2Fevidence%2Fquiz_074.png)
**Fig3. test of quiz 074**
