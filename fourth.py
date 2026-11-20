def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    
    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]
    
    # 1. KROK: Je cílová pozice na šachovnici? (řádky i sloupce 1 až 8)
    # Zde student napíše jednoduchou podmínku s and / or
    if cilova_pozice[0] < 1 or cilova_pozice[0] > 8 or cilova_pozice[1] < 1 or cilova_pozice[1] > 8:
        return False
    
    # 2. KROK: Je cílová pozice volná?
    # Nápověda: operátor 'in' nebo 'not in' pro množiny
    if cilova_pozice in obsazene_pozice:
        return False
    
    # 3. KROK: Pohyb podle typu figury
    if typ == "král":
        # Král se může pohnout maximálně o 1 pole v jakémkoliv směru.
        # Nápověda: rozdíl řádků a sloupců (absolutní hodnota abs()) musí být <= 1.
        rozdil_radku = abs(cilova_pozice[0] - aktualni_pozice[0])
        rozdil_sloupec = abs(cilova_pozice[1] - aktualni_pozice[1])

        if rozdil_radku <= 1 and rozdil_sloupec <= 1:
            return True
        
    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru L (např. rozdíl řádků je 2 a sloupců 1, nebo naopak).
        rozdil_radku = abs(cilova_pozice[0] - aktualni_pozice[0])
        rozdil_sloupec = abs(cilova_pozice[1] - aktualni_pozice[1])

        if (rozdil_radku == 2 and rozdil_sloupec == 1) or (rozdil_radku == 1 and rozdil_sloupec == 2):
            return True
        
    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # False (neni tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
