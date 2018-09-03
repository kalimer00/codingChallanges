import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input("Wieviele ISBN Nummer: "))

for i in range(n):
    # I_isbn exemple 030640615
    I_isbn = input("Eingabe der ISBN: ").strip()
    arr_I_isbn_check = [10,9,8,7,6,5,4,3,2]
    arr_II_isbn_check = [1,3,1,3,1,3,1,3,1,3,1,3]
    arr_I_isbn = [int(i) for i in str(I_isbn)]

    if len(arr_I_isbn) == 9:
        I_isbn_mal = np.multiply(arr_I_isbn_check, arr_I_isbn)
        I_isbn_sum = np.sum(I_isbn_mal)

        I_isbn_rest = I_isbn_sum % 11
        I_isbn_sum_new = I_isbn_sum

        while I_isbn_rest > 0:
            I_isbn_sum_new += 1
            I_isbn_rest = I_isbn_sum_new % 11

        I_isbn_digit = I_isbn_sum_new - I_isbn_sum
        arr_I_isbn.insert(9, I_isbn_digit)
        
    elif len(arr_I_isbn) == 12:
        # Testzahl 978030640615
        II_isbn_mal = np.multiply(arr_II_isbn_check, arr_I_isbn)
        II_isbn_sum = np.sum(II_isbn_mal)

        II_isbn_rest = II_isbn_sum % 10
        II_isbn_sum_new = II_isbn_sum

        while II_isbn_rest > 0:
            II_isbn_sum_new += 1
            II_isbn_rest = II_isbn_sum_new % 10

        II_isbn_digit = II_isbn_sum_new - II_isbn_sum
        arr_I_isbn.insert(12, II_isbn_digit)

    elif len(arr_I_isbn) >= 8 and len(arr_I_isbn) > 9:
        print("Fuck you!")

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if len(arr_I_isbn) == 9:
    print("ISBN: ", *arr_I_isbn)
    print("Multiplikator: ", *arr_I_isbn_check)
    print("Produkt der Arrays: ", *I_isbn_mal)
    print("Summe mit Rest: ", I_isbn_sum)
    print("Summe ohne Rest: ", I_isbn_sum_new)
    print("End Zahl: ", I_isbn_digit)
    
elif len(arr_I_isbn) == 12:
    print("ISBN: ", *arr_I_isbn)
    print("Multiplikator: ", *arr_II_isbn_check)
    print("Produkt der Arrays: ", *II_isbn_mal)
    print("Summe mit Rest: ", II_isbn_sum)
    print("Summe ohne Rest: ", II_isbn_sum_new)
    print("End Zahl: ", II_isbn_digit)
    
elif len(arr_I_isbn) >= 8 and len(arr_I_isbn) > 9:
    print("Gacke!")
