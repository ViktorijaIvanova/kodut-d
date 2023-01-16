from math import*
from random import*
#harjutus 0.2
katsed=0
answer=""
while answer!="10111":
    answer=input("palun kirjutage postindeks!")
    katsed+=1
    print(f"katsed: {katsed}")
    print()





#harjutus0.1
print("palun kirjutage postindeks")
katsed=0
while True:
    answer=input("palun kirjutage postindeks!")
    katsed +=1
    if answer.lower()=="10111":
        print(f"teil postindeks kirjutakse kulus {katsed} katse.")
        break



import random
#Harjutus 8.1
a = random.randint(1, 100)
a = int(input("sisetaga number:"))
while a < 101:
    if a % 2 == 0:
        print("paaris number")
        print("tsükkel on lõpp")
    elif a % 2 == 1:
        print("paaritu number")
        print("tsükkel on lõpp")
    break
else:
    print("Proovige veel üks kord")
    
    
    
#Harjutus 8.2
from math import*

a = int(input("sisetage number:"))

while True:
        if a <= 100:
            print(a)
            if a % 2 == 0:
                print("paaris number")
                print("tsükkel on lõpp")
            elif a % 2 == 1:
                print("paaritu number")
                print("tsükkel on lõpp")
            break
        
        else:
            print("Proovige veel kord")
            break
            
            




#22
print("ma tahan kommi")
katsed=0
while True:
    answer=input("tahan kommi!")
    katsed +=1
    if answer.lower()=="komm":
        print(f"teil kommid kirjutakse kulus {katsed} katse.")
        break
    #22.2
katsed=0
answer=""
while answer!="komm":
    answer=input("tahan kommi!")
    katsed+=1
    print(f"katsed: {katsed}")
    print()
#0
p=0
while True:
    number=int(input("sisestage number suurem kui 10: "))
    p+=1
    if number >=10:
        print("õigesti")
        break
    else:
        print("arv on liiga väike",)
print("katsed",p)




#ülesane 11
print("arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõistatanud arvutit?:  "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvunud ära, proovi uuesti!:  ")
    vastus=int(input("sisesta vastus:  "))
    k+=1
    p+=1
    if k>2:
        print("püüdlused on lõppenud")
        b=input("proovi veel kord")
        if b.upper()=="JÄH":
         k=0
         continue
        else:
            break
if vastus==a:
    print("palju õnne;sa arvasid ära!",p)
print() 

#harjutus 6
n=0
print ("*kolmnurga")
for e in range (11,0,-1):
    n = n+1
    for f in range (0, n+1):
        print ("*", end = "")
    print()
print("")



         

#Harjutus 0.1
indeks=int(input("Kirjuta oma postindeksi: "))#12345
a=5

while len(str(indeks)) == a:
    print("See on sinu postindeks")
    print(indeks)#12345
    break
else:
    print('Ebakorrektne indeks, indeksil on peab olema 5 tähti')
    


#Harjutus 0.2
while True:
    try:
        indeks = input("Kirjuta oma postindeksi: ")#12345
        if (5 == len(indeks) and indeks.isdigit()):
            break
        else:
            print('Ebakorrektne indeks, indeksil on peab olema 5 tähti')
    except :
        print("Viga")
print("See on sinu postindeks")
print(indeks)#12345

            

