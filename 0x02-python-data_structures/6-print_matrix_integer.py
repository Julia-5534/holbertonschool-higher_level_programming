#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            print("{:>3}".format(item), end=" ")
        print()

# This function takes in a matrix of integers as an argument and iterates through each row and item in the matrix.
# For each item, it uses the str.format() method to format the integer as a string with a width of 3 and right-aligns
# it. The end parameter is set to a space, so that the integers are separated by a space. After each row, it adds a
# newline character using print() method to separate each row in the matrix.
