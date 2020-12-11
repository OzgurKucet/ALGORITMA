# -*- coding: utf-8 -*-

#abc +def = kmnp her farklı harf farklı bir rakamı temsil eder
#bu koşulu sağlayan tüm sayilari bul.

def ListeElemanlarıFarklıMı(liste):
    bakılan = liste[0]
    for i in range(1,len(liste)):
        for j in range(i,len(liste)):
            if(bakılan == liste[j]):
                return 0
        bakılan = liste[i]

    return 1

def SayınınBasamaklarınıListeyeAlma(sayi):
    liste = []
    while sayi!=0:
        a = int(sayi%10)
        sayi = int(sayi/10)
        liste.append(a)
    return ListeElemanlarıFarklıMı(liste)


for i in range(100,1000):
    for j in range(100,1000):
        if i+j<1000:
            continue
        else:
            yanyanakoy = str(i)+str(j)+str(i+j)
            yanyanakoy = int(yanyanakoy)
            if SayınınBasamaklarınıListeyeAlma(yanyanakoy):
                print(i,"+",j,"=",i+j)


