#import bibliotek
import math

switch_to_dec = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

lit_ord = [65, 66, 67, 68, 69, 70]
num_ord = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

# zamiana liczby binarnej na system dziesietny
def bin_to_dec (liczba_bin = []):
    # definicja zmiennych
    # dlugosc listy sprawdzana celem wyznaczenia najwyzszej potegi ciagu liczb binarnych
    ilosc_iteracji = liczba_bin.__len__()
    # obliczenie potegi z uwzglednieniem 0
    potega = ilosc_iteracji - 1
    # zmienne do realizacji petli
    liczba_dec = 0
    i = 0

    for i in range(ilosc_iteracji):
        # skladowa pierwsza wyciagajaca kolejny element listy
        sk_1 = liczba_bin[i]
        # skladowa druga obliczajaca 2 podenisiona do potegi, mnozenie przez pierwsza skladowa wyklucza 0 i bierze pod uwage tylko elementy gdy w ciagu liczb binarnych wystapi 1
        sk_2 = math.pow(2, potega) * sk_1
        # sumowanie poszczegolnych liczb
        liczba_dec = liczba_dec + sk_2
        # modyfikacja wartosci dla poprawnej realizacji petli
        potega -= 1

    return liczba_dec

# Zmiana liczby osemkowej na dziesietny
def oct_to_dec(liczba_oct = []):
    # Definicja zmiennych
    liczba_dec = 0
    # dlugosc listy sprawdzana celem wyznaczenia najwyzszej potegi ciagu liczb ósemkwoych
    ilosc_iteracji = liczba_oct.__len__()
    potega =ilosc_iteracji - 1
    # zmienna do realizacji pętli
    i = 0

    for i in range(ilosc_iteracji):
        # skladowa pierwsza wyciagajaca kolejny element listy
        sk_1 = liczba_oct[i]
        # skladowa druga obliczana przez potege liczby 8 pomnozona przez liczbe wyciagnieta z listy
        sk_2 = math.pow(8,potega)*sk_1
        # sumowanie poszczegolnych liczb
        liczba_dec = liczba_dec + sk_2
        # modyfikacja wartosci dla poprawnej realizacji petli
        potega -= 1

    return liczba_dec

# Zmiana liczby szesnanstkowej na liczbe dziesietna
def heks_to_dec(liczba_heks = []):
    #definicja zmiennych
    liczba_dec = 0
    # dlugosc listy sprawdzana celem wyznaczenia najwyzszej potegi ciagu liczby sensnastkowej
    ilosc_iteracji = liczba_heks.__len__()
    # obliczenie wartosci najwyzszej potegi
    potega = ilosc_iteracji - 1

    for i in range(ilosc_iteracji):
        # skladowa pierwsza wyciagajaca i-ty element
        sk_1 = liczba_heks[i]
        # jesli skladowa pierwsza jest typu string przypisanie odpowiedniej wartosci dla litery w ciagu liczby szesnastkowej
        if type(sk_1) == str:
            sk_2 = switch_to_dec.get(sk_1)
        # w innym wypadku skladowa druga jest rowna skladowej pierwszej
        else:
            sk_2 = sk_1
        # skladowa trzecia obliczana przez potege liczby 16 pomnozona przez liczbe przechowywana w ciagu liczb szesnastkowym
        sk_3 = math.pow(16, potega) * sk_2
        # sumowanie poszczegolnych liczb
        liczba_dec = liczba_dec + sk_3

        potega -= 1

    return liczba_dec
