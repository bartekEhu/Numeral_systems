import math

# Elements used in the creation of the hexadecimal system
switch_from_dec = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }


def dec_to_bin(liczba_dec):
    """Function responsible for changing a number from decimal to binary"""

    potega = 0
    liczba_bin = []
    liczba_bin_str = ''

    liczba_dec = int(liczba_dec)

    # Calculation of the highest power
    while (liczba_dec - math.pow(2, potega)) >= 0:
        potega += 1

    # Correct for the loop
    potega = potega - 1

    while potega > -1:
        odejmowana = math.pow(2, potega)

        # Assigning 1 if the set number is greater than the one to be subtracted
        # and assigning 1 to a series of binary numbers
        if liczba_dec >= odejmowana:
            liczba_dec = liczba_dec - odejmowana
            liczba_bin.append(1)
            liczba_bin_str += '1'
            potega -= 1

        # Else assign 0 and do not reduce the set number
        elif liczba_dec < odejmowana:
            liczba_bin.append(0)
            liczba_bin_str += '0'
            potega -= 1

    return liczba_bin, liczba_bin_str


def dec_to_heks(liczba_dec):
    """Function responsible for changing a number from decimal to hexadecimal"""

    liczba_heks = []
    liczba_heks_str = ''

    liczba_dec = int(liczba_dec)

    # Assignment of a value when the preset number is between 0 and 15
    if liczba_dec < 16:
        if liczba_dec <= 9:
            liczba_heks.append(liczba_dec)
            x = str(liczba_dec)
            liczba_heks_str += x

        elif liczba_dec > 9:
            liczba_heks.append(switch_from_dec.get(liczba_dec))

    if liczba_dec >= 16:
        while liczba_dec > 0:
            reszta = liczba_dec % 16

            # Assignment of 0-9 or the corresponding letter A-F depending on the remainder of the division
            if reszta <= 9:
                liczba_heks.append(reszta)

            if reszta > 9:
                liczba_heks.append(switch_from_dec.get(reszta))

            # Decreasing the value of a passed number by dividing by 16 and retaining the whole number
            liczba_dec = int(liczba_dec/16)

    # Inverting the list in order to maintain the correct record
    liczba_heks.reverse()

    hex_str_ln = len(liczba_heks)
    for i in range(hex_str_ln):
        op1 = str(liczba_heks[i])
        liczba_heks_str += op1

    return liczba_heks, liczba_heks_str


def dec_to_oct(liczba_dec):
    """Function responsible for changing a number from decimal to octal"""

    liczba_oct = []
    liczba_oct_str = ''

    liczba_dec = int(liczba_dec)

    if liczba_dec < 8:
        liczba_oct.append(liczba_dec)

    if liczba_dec >= 8:
        while liczba_dec > 0:
            reszta = liczba_dec % 8

            # Assigning values depending on the remainder of the division
            liczba_oct.append(reszta)

            # Decreasing the value of a passed number by dividing by 16 and retaining the whole number
            liczba_dec = int(liczba_dec/8)

    # Inverting the list in order to maintain the correct record
    liczba_oct.reverse()

    oct_str_ln = len(liczba_oct)
    for i in range(oct_str_ln):
        op1 = str(liczba_oct[i])
        liczba_oct_str += op1

    return liczba_oct, liczba_oct_str