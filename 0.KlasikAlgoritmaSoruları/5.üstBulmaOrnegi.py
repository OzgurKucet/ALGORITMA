def power1(a,b):
    sonuc = 1
    if a==0:
        return 0
    elif b==0:
        return 1
    elif b == 1:
        return a
    else:
        for i in range(b):
            sonuc *= a
        return sonuc

def power2(a,b):#recursive yazdim...
    if b == 0:
        return 1
    if b == 1:
        return a
    if b>1:
        return power2(a,b-1)*a

print(power1(2,5))
print(power2(2,0))
