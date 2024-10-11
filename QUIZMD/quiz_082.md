# Quiz082!
[quiz_082.png](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_082.png)
**Fig1. Quiz 082**

![quiz_082.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_082.jpeg)
**Fig2. Note Quiz 082 No.1**
![quiz_082-2.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_082-2.jpeg)
**Fig2. Note Quiz 082 No.2**

## 1.solution
```.py
def FUNC(N):
    if N == 1 or N == 0:
        return 1

    else:
        return N * FUNC(N - 1)

test=FUNC(N=7)
print(test)
```

## 2.proof of work
![quiz_082.png](..%2FImage%2Fevidence%2Fquiz_081-088%2Fquiz_082.png)
**Fig3. test of quiz 082**
