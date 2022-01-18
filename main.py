'''
1.3 Feladat
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb páros számot!

'''

szamlista = []
paros_lista = []


while True:
  szam = input("Kérek egy számot! ")
  if szam == "":
    break
  else:
    szamlista.append(int(szam))
    if int(szam) % 2 == 0:
      paros_lista.append(int(szam))

print(f"A lista elemei:  {szamlista} ")
print(f"A legkisebb páros szám:  {min(paros_lista)} ")
print(f"A legnagyobb páros szám: {max(paros_lista)} ")    