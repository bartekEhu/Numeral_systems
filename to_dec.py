import math

# Elements used in the read the hexadecimal system
switch_to_dec = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

# Character codes for checking whether a given value occurs in a given system, lit_ord for A-F, num_ord for 0-9,
# this eliminates the need to constantly change types
lit_ord = [65, 66, 67, 68, 69, 70]
num_ord = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]


def bin_to_dec(liczba_bin):
    """Function responsible for changing a number from binary to decimal"""
    # Finding the greatest power of binary number
    ilosc_iteracji = liczba_bin.__len__()
    # Correct because of 0
    potega = ilosc_iteracji - 1

    liczba_dec = 0

    for i in range(ilosc_iteracji):
        # sk_1 and sk_2 these are the variables used for calculations inside the loop
        sk_1 = liczba_bin[i]
        sk_2 = math.pow(2, potega) * sk_1

        liczba_dec = liczba_dec + sk_2

        potega -= 1

    return liczba_dec


def oct_to_dec(liczba_oct):
    """Function responsible for changing a number from octal to decimal"""
    liczba_dec = 0
    # Finding the greatest power of octal number
    ilosc_iteracji = liczba_oct.__len__()
    # Correct because of 0
    potega = ilosc_iteracji - 1

    for i in range(ilosc_iteracji):
        # sk_1 and sk_2 these are the variables used for calculations inside the loop
        sk_1 = liczba_oct[i]
        sk_2 = math.pow(8, potega)*sk_1

        liczba_dec = liczba_dec + sk_2

        potega -= 1

    return liczba_dec


def heks_to_dec(liczba_heks):
    """Function responsible for changing a number from octal to hexadecimal"""
    liczba_dec = 0
    # Finding the greatest power of hexadecimal number
    ilosc_iteracji = liczba_heks.__len__()
    # Correct because of 0
    potega = ilosc_iteracji - 1

    for i in range(ilosc_iteracji):
        sk_1 = liczba_heks[i]
        # Checking the type of element tested, for str assigning the appropriate letter
        if type(sk_1) == str:
            sk_2 = switch_to_dec.get(sk_1)
        # Else the value is prescribed
        else:
            sk_2 = sk_1

        sk_3 = math.pow(16, potega) * sk_2

        liczba_dec = liczba_dec + sk_3

        potega -= 1

    return liczba_dec
