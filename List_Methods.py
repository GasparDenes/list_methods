#szamok = [5, 2, 1, 7, 4]
#szamok2 = [6, 3, 8, 6, 14]

#szamok.append(20)       #Szám hozzáadása a lista végére.
#szamok.insert(0, 10)    #Szám hozzáadása, ahol az 1. érték az indexet adja meg,
                        #a 2. érték pedig magát a a számot.
#szamok.remove(7)        #Szám törlése a listából.
#szamok.clear()          #Összes szám törlése a listából.

#szamok2.pop()            #Utolsó szám törlése a listából.
#szamok2.index(14)        #Egy adott érték indexét keresi meg a listában.
                         #Ha az érték nincs a listában, errorral zár a program. 

#25 in szamok2            #Egy boolean-t ad vissza:ha a szám benne van a listában, akkor True,
                         #ha nincs, akkor False
#szamok2.count(6)         #Megnézi, hogy az adott érték hányszor fordul elõ a listában.

#szamok2.sort()           #Növekvõ sorrendbe rendezés.
#szamok2.reverse()        #Csökkenõ sorrendbe rendezés.

#szamok3 = szamok2.copy() #Egy másolatot csinál egy megadott listáról.Ha a lista megváltozik,
                         #akkor a másolat is frissülni fog.

#Feladat: írjunk egy programot, ami a többször elõforduló számokat kitörli!

#1.Megoldás:

szamok4 = [3, 9, 9, 5, 2, 3]

for i in szamok4:
    if szamok4.count(i) == 2:
        szamok4.remove(i)
print(szamok4)

#2.Megoldás:

szamok5 = szamok4.copy()
kulonallo = []

for szam in szamok5:
    if szam not in kulonallo:
        kulonallo.append(szam)

