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