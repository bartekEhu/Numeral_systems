#sekcja odpowiadajaca za zamiane liczby w wsystemie dziesietnym na pozostale systemy liczbowe

#import bibliotek
import math

switch_from_dec = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }

#################################################################################dziesietna na binarna########################################################################################


def dec_to_bin(liczba_dec):
    #deklaracja wartosci poczatkaowych zmiennych - wartosc potegi i liczby binarnej
    potega = 0
    liczba_bin = []
    liczba_bin_str = ''

    liczba_dec = int(liczba_dec)

    #wyliczenie najwiekszej potegi2
    while (liczba_dec - math.pow(2, potega)) >= 0:
        potega += 1

    #ograniczenie potegi na potrzeby petli
    potega = potega - 1

    #obliczanie liczby binarnej
    while potega > -1:
        #obliczenie wartosci odejmowanej od wartosci zadanej
        odejmowana = math.pow(2, potega)

        #przypisanie 1 w przypadku gdy liczba zadana jest wieksza od odejmowanej oraz przypisanie 1 do szeregu liczby binarnej
        if liczba_dec >= odejmowana:
            liczba_dec = liczba_dec - odejmowana
            liczba_bin.append(1)
            liczba_bin_str += '1'
            potega -= 1

        #w innym przypadku przypisanie 0 oraz nie zmniejszanie liczby zadanej
        elif liczba_dec < odejmowana:
            liczba_bin.append(0)
            liczba_bin_str += '0'
            potega -= 1


    #zwrocenie liczby binarnej
    return liczba_bin, liczba_bin_str

############################################################################dziesietna na szesnastkowa##############################################################################################



def dec_to_heks (liczba_dec):
    #deklaracja listy
    liczba_heks = []
    liczba_heks_str = ''

    liczba_dec = int(liczba_dec)

    #przypisanie wartosci w przypadku gdy liczba zadana zawiera się od 0 do 15
    if liczba_dec < 16:
        if liczba_dec <= 9:
            liczba_heks.append(liczba_dec)
            x = str(liczba_dec)
            liczba_heks_str += x

        elif liczba_dec > 9:
            liczba_heks.append(switch_from_dec.get(liczba_dec))

    #rozwiazanie zadanej liczby
    if liczba_dec >= 16:

        while liczba_dec > 0:
            #sprawdzenie reszty dzielenia
            reszta = liczba_dec % 16

            #przypsianie wartosci zaleznie od reszty z dzielenia
            if reszta <= 9:
                liczba_heks.append(reszta)

            if reszta > 9:
                liczba_heks.append(switch_from_dec.get(reszta))

            #zmniejszanie wartosci liczby zdanej przez dzielenie przez 16 i zachowanie liczby calkowitej
            liczba_dec = int(liczba_dec/16)

    #odwrocenie listy celem zachowania odpowiedniego zapisu
    liczba_heks.reverse()

    hex_str_ln = len(liczba_heks)
    for i in range(hex_str_ln):
        op1 = str(liczba_heks[i])
        liczba_heks_str += op1

    #zwrocenie liczby w systemie szesnatskowym
    return liczba_heks, liczba_heks_str

######################################################################################dziesietna na osemkowy####################################################################################



def dec_to_oct(liczba_dec):
    liczba_oct = []
    liczba_oct_str = ''

    liczba_dec = int(liczba_dec)

    if liczba_dec < 8:
        liczba_oct.append(liczba_dec)

    #rozwiazanie zadanej liczby
    if liczba_dec >= 8:
        while liczba_dec > 0:
            #sprawdzenie reszty dzielenia
            reszta = liczba_dec % 8

            #przypsianie wartosci zaleznie od reszty z dzielenia
            liczba_oct.append(reszta)

            #zmniejszanie wartosci liczby zdanej przez dzielenie przez 16 i zachowanie liczby calkowitej
            liczba_dec = int(liczba_dec/8)

    #odwrocenie listy celem zachowania odpowiedniego zapisu
    liczba_oct.reverse()

    #odwrocenie stringa
    oct_str_ln = len(liczba_oct)
    for i in range(oct_str_ln):
        op1 = str(liczba_oct[i])
        liczba_oct_str += op1

    return liczba_oct, liczba_oct_str