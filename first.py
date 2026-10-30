def sude_nebo_liche(x):
    vysledek = x % 2
    if vysledek == 0:
        aa = "sudé"
    else:
        aa = "liché"
    return aa

if __name__ == "__main__":
    #x = secti(1,2,3)
    #print("Vysledek:",x)
    cislo=5
    x = sude_nebo_liche(cislo)
    print("Číslo",cislo,"je",x)

    cislo=1000000
    x = sude_nebo_liche(cislo)
    print("Číslo",cislo,"je",x)