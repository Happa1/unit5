# Quiz073
![quiz_073.jpg](..%2FImage%2Fqustion%2Fquiz_073.jpg)
**Fig1. Quiz 073**

![quiz_073.jpeg](..%2FImage%2Fnote%2Fquiz_073.jpeg)
**Fig2. Note Quiz 073**

## 1.solution
```.py
n = str(input("Please enter the message"))
count=0
error=True

for i in range(1, len(n)):
    if n[i]=='1':
        count+=1

if count%2!=int(n[0]):
    error=False

if error == True:
    print("This is an error message.")

else:
    print("This is not an error message.")
```

## 2.proof of work
![quiz_073_error.png](..%2FImage%2Fevidence%2Fquiz_073_error.png)
**Fig3. test of quiz 073 (Error case)**

![quiz_073.png](..%2FImage%2Fevidence%2Fquiz_073.png)
**Fig4. test of quiz 073 (Not Error case)**


