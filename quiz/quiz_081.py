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