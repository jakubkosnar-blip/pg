import time

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.
    Využívá efektivní algoritmus s odmocninou a skoky po 6.
    """
    cislo = int(cislo)
    
    # Čísla menší nebo rovna 1 nejsou prvočísla
    if cislo <= 1:
        return False
        
    # 2 a 3 jsou prvočísla
    if cislo <= 3:
        return True
        
    # Pokud je číslo dělitelné 2 nebo 3, není to prvočíslo
    if cislo % 2 == 0 or cislo % 3 == 0:
        return False
        
    # Kontrola dělitelnosti od 5 do odmocniny čísla se skoky po 6
    # Testujeme vždy dvojice (delitel) a (delitel + 2), což odpovídá formátu 6k +/- 1
    hranice = round(cislo ** 0.5)
    delitel = 5
    
    while delitel <= hranice:
        time.sleep(0.001)  
        
        if cislo % delitel == 0 or cislo % (delitel + 2) == 0:
            return False
            
        delitel += 6  # Skočíme na další násobek 6 (např. z 5 na 11)
        
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    maximum = int(maximum)
    results = []
    
    # Procházíme všechna čísla od 1 do maximum
    for i in range(1, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
            
    return results

# --- Otestování programu podle příkladů v zadání ---
if __name__ == "__main__":
    # Test první funkce (je_prvocislo)
    print("--- Test funkce je_prvocislo ---")
    print(f"1 -> {je_prvocislo(1)}")
    print(f"2 -> {je_prvocislo(2)}")
    print(f"3 -> {je_prvocislo(3)}")
    print(f"100 -> {je_prvocislo(100)}")
    print(f"101 -> {je_prvocislo(101)}")

    # Test druhé funkce (vrat_prvocisla)
    print("\n--- Test funkce vrat_prvocisla ---")
    print(f"1 -> {vrat_prvocisla(1)}")
    print(f"2 -> {vrat_prvocisla(2)}")
    print(f"3 -> {vrat_prvocisla(3)}")
    print(f"10 -> {vrat_prvocisla(10)}")
