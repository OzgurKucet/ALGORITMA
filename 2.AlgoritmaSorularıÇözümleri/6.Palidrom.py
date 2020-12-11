# -*- coding: utf-8 -*-
import random

def palidrom_mu(liste):
    for i in range(0,int(len(liste)/2)):
        if(liste[i] != liste[-i-1]):
            return -1
    return 1


def palidrom_olmasini_sagla(liste):
    for i in range(0,int(len(liste)/2)):
        if(liste[i]=="?" and liste[-i-1]=="?"):
            harf = harfler[random.randint(0,20)]
            liste[i] = harf
            liste[-i-1] = harf
        elif(liste[i]=="?"):
            liste[i] = liste[-i-1]
        elif(liste[-i-1]=="?"):
            liste[-i-1]=liste[i]
    return liste

harfler = ["a","b","c","d","e","f","g","h","ı","l","k","m","n","o","p","r","s","t","u","v","y""z"]

liste = []
while(1):
    print("Listenin harflerini teker teker girin (ornek a) listeyi tamam ise -1 girin")
    harf=input()
    harf = harf.lower()
    if(harf=="-1"):
        break
    liste.append(harf)



print("girdiğiniz liste: ",liste)
liste = palidrom_olmasini_sagla(liste)
if(palidrom_mu(liste)==1):
    print("palidrom:",liste)
else:
    print("Hayır")
