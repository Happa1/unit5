# Quiz084
![quiz_084.jpg](..%2FImage%2Fqustion%2Fquiz_081-088%2Fquiz_084.jpg)
**Fig1. Quiz 084**

![quiz_084.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_084.jpeg)
**Fig2. Note Quiz 084 No.1**
![quiz_084-2.jpeg](..%2FImage%2Fnote%2Fquiz_081-088%2Fquiz_084-2.jpeg)
**Fig2. Note Quiz 084 No.2**

## 1.solution
```.py
def merge_sort(m:list):
    if len(m)<=1:
        return m
    n=len(m)//2
    l=merge_sort(m[:n])
    r=merge_sort(m[n:])
    s,i,j=[],0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            s.append(l[i])
            i+=1
        else:
            s.append(r[j])
            j+=1
    return s+l[i:]+r[j:]

test=merge_sort(m=[3,1,8,7,2,5])
print(test)
```

## 2.proof of work
![quiz_084.png](..%2FImage%2Fevidence%2Fquiz_081-088%2Fquiz_084.png)
**Fig3. test of quiz 084**
