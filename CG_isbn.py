import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input("Wieviele ISBN Nummer: "))


for i in range(n):
    # isbn exemple 030640615
    isbn = input("Eingabe der ISDN: ").strip()
    arr_isbn_check = [10,9,8,7,6,5,4,3,2]
    arr_isbn = [int(i) for i in str(isbn)]

    isbn_mal = np.multiply(arr_isbn_check, arr_isbn)
    isbn_sum = np.sum(isbn_mal)

    isbn_rest = isbn_sum % 11
    while isbn_rest > 0:
        isbn_sum += 1
        isbn_rest = isbn_sum % 11
        #print(isbn_rest)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
    print("Isbn: ", *arr_isbn)
    print("Multiplikator: ", *arr_isbn_check)
    print("Produkt der Arrays: ", *isbn_mal)
    print("Summe ohne Rest: ", isbn_sum)
    print("Rest: ", isbn_rest)
