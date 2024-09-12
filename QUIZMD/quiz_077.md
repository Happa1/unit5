# Quiz077
![quiz_077.jpg](..%2FImage%2Fqustion%2Fquiz_077.jpg)
**Fig1. Quiz 077**

![quiz_077.jpeg](..%2FImage%2Fnote%2Fquiz_077.jpeg)
**Fig2. Note Quiz 077**

## 1.solution
```.py
def get_check_p(len_msg,p):
    output=[]
    for i in range(len_msg+1):
        n = i & (2 ** p)
        if n:
            output.append(i-1)
    return output

test=get_check_p(7,0)
print(test)
```

## 2.proof of work
![quiz_077.png](..%2FImage%2Fevidence%2Fquiz_077.png)
**Fig3. test of quiz 077**

