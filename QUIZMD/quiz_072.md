# Quiz072
![quiz_072.jpg](..%2FImage%2Fqustion%2Fquiz_072.jpg)
**Fig1. Quiz 072**

![quiz_072.PNG](..%2FImage%2Fnote%2Fquiz_072.PNG)
**Fig2. Note Quiz 072**

## 1.solution
```.py
def get_lists(data:list):
    city=[]
    country=[]
    for i in range(0,len(data),2):
        city.append(data[i])
        country.append(data[i+1])
    return city, country

test=get_lists(data=['Ankara','Turkey','Tokyo','Japan','Lisbon', 'Portugal'])
print(test)


```

## 2.proof of work
![quiz_072.png](..%2FImage%2Fevidence%2Fquiz_072.png)
**Fig3. test of quiz 072**
