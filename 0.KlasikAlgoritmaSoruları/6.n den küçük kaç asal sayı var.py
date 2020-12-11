def kacasal(n):
    sayac = 0
    while n > 2:
        i=3
        if n == 3:
            return(sayac+2)
        if int(n/2)*2==n:
            n=n-1
            continue
        while i<n-2:
            if int(n/i)*i==n:
                n=n-1
                continue

            i=i+2
        sayac += 1
        print(n)
        n -= 1
    return(sayac)

print(kacasal(8))
# 2,3,5,7,11,13,17,19,23,27,29,31,37
