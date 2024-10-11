# Quiz083
![quiz_083.jpg](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_083.jpg)
**Fig1. Quiz 083**

![quiz_083.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_083.jpeg)
**Fig2. Note Quiz 083**

## 1.solution
```.py
def FUNC(N):
    if len(N) == 1:
        return N[0]
    else:
        mid = len(N) // 2
        L = FUNC(N[:mid])
        R = FUNC(N[mid:])
    return L + R

test=FUNC(N=[5,3,1,10])
print(test)
```

## 2.proof of work
![quiz_083.png](..%2FImage%2Fevidence%2Fquiz_081-088%2Fquiz_083.png)
**Fig3. test of quiz 083**
