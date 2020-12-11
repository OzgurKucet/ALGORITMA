def allprimes(n):
    """bir sayıdan küçük bütün asal sayıları dizi olarak döndüren fonksiyon"""
    primes=[]
    for i in range(2,n+1):
        primes.append(i)
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])

n = int(input("bir sayi girin:"))
print(len(allprimes(n)))
print(allprimes(n))
print(allprimes(100))
