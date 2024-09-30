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