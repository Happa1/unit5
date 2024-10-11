# Quiz088
![quiz_088.jpg](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_088.jpg)
**Fig1. Quiz 088**

![quiz_088.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_088.jpeg)
**Fig2. Note Quiz 088**

## 1.solution
```.py
from quiz_087 import Stack
def quiz_088(rpn):
    stack=Stack()
    for value in rpn:
        if isinstance(value, int):
            stack.push(value)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if value == "+":
                new_value=operand1 + operand2
                stack.push(new_value)
            elif value == "-":
                new_value=operand1 - operand2
                stack.push(new_value)
            elif value == "*":
                new_value=operand1 * operand2
                stack.push(new_value)
            elif value == "/":
                new_value=operand1 / operand2
                stack.push(new_value)
    result=stack.pop()
    return f"The result is: {result}"

test=quiz_088(rpn=[5,2,"+",25,16,"-","*",3,"/"])
print(test)



```

## 2.proof of work
![quiz_088.png](..%2FImage%2Fevidence%2Fquiz_081-088%2Fquiz_088.png)
**Fig3. test of quiz 088**
