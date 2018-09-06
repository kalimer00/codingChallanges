# coding=utf-8
import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())


def isbn_check(isbn, ref_isbn, div, art_isbn):
    arr_isbn = [int(i) for i in isbn]
    arr_multiply = np.multiply(arr_isbn, ref_isbn)
    sume = np.sum(arr_multiply)

    rest = sume % div
    sume_new = sume

    while rest > 0:
        sume_new += 1
        rest = sume_new % div

    digit = sume_new - sume
    arr_isbn.insert(art_isbn, digit)

    print("Array mal Produkt: ", arr_multiply)
    print("Sume: ", sume)
    print("Rest: ", rest)
    print("Zahl: ", digit)
    print("Dividenten: ", div)
    print("Neue Sume: ", sume_new)
    print("Array mal: ", ref_isbn)
    print("ISBN: ", arr_isbn)


for i in range(n):
    isbn = input()
    # test: 030640615
    ref_isbn_10 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    # test: 978030640615
    ref_isbn_13 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]

    if isbn.isdigit() and len(isbn) == 9:
        isbn_check(isbn, ref_isbn_10, 11, 9)
    else:
        print(isbn)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
