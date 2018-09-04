import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input("Wie viele ISBN Nummer: "))


def isbn(arr_isbn_check, arr_isbn, div, iban_stellen):
    # I_isbn exemple 030640615
    isbn_mal = np.multiply(arr_isbn_check, arr_isbn)
    isbn_sum = np.sum(isbn_mal)

    isbn_rest = isbn_sum % div
    isbn_sum_new = isbn_sum

    while isbn_rest > 0:
        isbn_sum_new += 1
        isbn_rest = isbn_sum_new % div

    isbn_digit = isbn_sum_new - isbn_sum
    arr_isbn.insert(iban_stellen, isbn_digit)

    print("ISBN: ", *arr_I_isbn)
    print("Multiplikator: ", *arr_isbn_check)
    print("Produkt der Arrays: ", *isbn_mal)
    print("Summe mit Rest: ", isbn_sum)
    print("Summe ohne Rest: ", isbn_sum_new)
    print("End Zahl: ", isbn_digit)


for i in range(n):
    I_isbn = input("Eingabe der ISBN: ").strip()
    arr_isbn_check10 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    arr_isbn_check13 = [1,3,1,3,1,3,1,3,1,3,1,3]
    arr_I_isbn = [i for i in str(I_isbn)]

    if len(I_isbn) == 9 and I_isbn.isdigit():
        isbn(arr_isbn_check10, arr_I_isbn, 11, 9)
    elif len(I_isbn) == 12 and I_isbn.isdigit():
        isbn(arr_isbn_check10, arr_I_isbn, 10, 12)
    else:
        print(I_isbn)
