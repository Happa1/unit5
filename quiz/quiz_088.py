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


