"""
Kendi yazdığım asal sayi bulan program
"""
def Asal_mi(sayi):
    if sayi == 1 or sayi == 2:
        return 1
    if(sayi%2==0):
        return 0
    if(sayi<1):
        return 0
    for i in range(sayi-2,1,-2):
        if(sayi%i==0):
            return 0
    return 1

"""
Daha Verimli Bir kod Daha az döngüde kalır...:
"""
def isprime(a): #bir sayinin asalmı olduguna bakan fonksiyon
    i=3
    if(a<2):
        return(0)
    if a!=2 and a%2==0:
        return(0)
    while i<=a**(1/2):
        if a%i==0:
            return(0)
        i += 2
    return(1)
