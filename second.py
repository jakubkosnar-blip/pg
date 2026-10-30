def cislo_text(cislo):
   
    n = int(cislo)
    
    # Slovníky
    jednotky = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }
    
    nact = {
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 
        14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmáct", 
        18: "osmnáct", 19: "devatenáct"
    }
    
    desitky = {
        2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát", 
        6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
    }

    
    if 0 <= n <= 9:
        return jednotky[n]
        
    
    elif 10 <= n <= 19:
        return nact[n]
        
    
    elif 20 <= n <= 99:
        d = n // 10
        j = n % 10
        
        if j == 0:
            return desitky[d]
        else:
            return f"{desitky[d]} {jednotky[j]}"
            
    
    elif n == 100:
        return "sto"
        
    
    else:
        return "Číslo je mimo podporovaný rozsah (0-100)"


if __name__ == "__main__":
    print(cislo_text(0))
    print(cislo_text(1))
    print(cislo_text(15))
    print(cislo_text(25))    
    print(cislo_text(100))
