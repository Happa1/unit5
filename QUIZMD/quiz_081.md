# Quiz081
![quiz_081.png](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_081.png)
**Fig1. Quiz 081**

![quiz_081.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_081.jpeg)
**Fig2. Note Quiz 081**

## 1.solution
```.py
def swap_letter(s:str,k:int,i:int):
    s=list(s)
    temp1=s[k]
    temp2=s[i]
    s[k]=temp2
    s[i]=temp1
    return "".join(s)

def PERM(s:str, k:int):
    if k == len(s):
        return [s]
    else:
        out = []
        for i in range(len(s)):
            t = swap_letter(s, k, i)
            out.extend(PERM(t,k+1))
        return out

test=PERM(s='AB', k=1)
print(test)
```

## 2.proof of work
![quiz_081.jpg](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_081.jpg)
**Fig3. test of quiz 081**
