# 1 1 2 3 5 8 13 21 34 55
fib1 = 1
fib2 = 1

kac = int(input("Kacıncı fibonacci sayisi bulunsun:"))

for i in range(kac-2):
    fib = fib1+fib2
    fib1 = fib2
    fib2 = fib

print(fib)


