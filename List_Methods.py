#szamok = [5, 2, 1, 7, 4]
#szamok2 = [6, 3, 8, 6, 14]

#szamok.append(20)       #Sz�m hozz�ad�sa a lista v�g�re.
#szamok.insert(0, 10)    #Sz�m hozz�ad�sa, ahol az 1. �rt�k az indexet adja meg,
                        #a 2. �rt�k pedig mag�t a a sz�mot.
#szamok.remove(7)        #Sz�m t�rl�se a list�b�l.
#szamok.clear()          #�sszes sz�m t�rl�se a list�b�l.

#szamok2.pop()            #Utols� sz�m t�rl�se a list�b�l.
#szamok2.index(14)        #Egy adott �rt�k index�t keresi meg a list�ban.
                         #Ha az �rt�k nincs a list�ban, errorral z�r a program. 

#25 in szamok2            #Egy boolean-t ad vissza:ha a sz�m benne van a list�ban, akkor True,
                         #ha nincs, akkor False
#szamok2.count(6)         #Megn�zi, hogy az adott �rt�k h�nyszor fordul el� a list�ban.

#szamok2.sort()           #N�vekv� sorrendbe rendez�s.
#szamok2.reverse()        #Cs�kken� sorrendbe rendez�s.

#szamok3 = szamok2.copy() #Egy m�solatot csin�l egy megadott list�r�l.Ha a lista megv�ltozik,
                         #akkor a m�solat is friss�lni fog.

#Feladat: �rjunk egy programot, ami a t�bbsz�r el�fordul� sz�mokat kit�rli!

#1.Megold�s:

szamok4 = [3, 9, 9, 5, 2, 3]

for i in szamok4:
    if szamok4.count(i) == 2:
        szamok4.remove(i)
print(szamok4)

#2.Megold�s:

szamok5 = szamok4.copy()
kulonallo = []

for szam in szamok5:
    if szam not in kulonallo:
        kulonallo.append(szam)

