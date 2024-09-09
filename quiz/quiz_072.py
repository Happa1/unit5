def get_lists(data:list):
    city=[]
    country=[]
    for i in range(0,len(data),2):
        city.append(data[i])
        country.append(data[i+1])
    return city, country

test=get_lists(data=['Ankara','Turkey','Tokyo','Japan','Lisbon', 'Portugal'])
print(test)

