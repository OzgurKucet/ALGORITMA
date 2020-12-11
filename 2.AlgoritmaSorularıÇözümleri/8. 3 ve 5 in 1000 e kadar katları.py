"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

"""
3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48....
5 10 *15 20 25 *30 35 40 *45 50 55 *60 65 70 *75 80 85 *90....
"""
tektop = 0
cifttop = 0
aynısayilar = 0

for i in range(1,334):

    tektop += i*3

for i in range(1,201):

    cifttop += i*5

   # if aynısayilar < 1000:
   #     aynısayilar += (3*i)*5
for i in range(1,68):
        aynısayilar += (3*i)*5

toplam = tektop+cifttop-aynısayilar
print(toplam)

