def beker():
    szam1 = int(input())
    return szam1

def parosszam():
    i = 0
    szamok = []
    while i < 3:
        print(f"Kérem a {i+1}. páros számot! ")
        szam1 = beker()
        while szam1 % 2 != 0:
            szam1 = int(input("Ez nem páros! PÁROS számot kérek! "))
        szamok.append(szam1)
    i += 1
    return szamok

