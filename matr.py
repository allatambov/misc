# preparation

import sympy as sp

# add necessary letters here or import whole alphabet via import *

from sympy.abc import a, b, c, d  
sp.init_printing(use_unicode = False)
lamda = sp.Symbol('lamda')

# open file with matrix

filename = input("Enter file name: \n")
f = open(filename, "r")
lines = f.read().splitlines()
print("\n")

# create and print matrix from file

M = sp.Matrix([i.split() for i in lines])
print("Matrix M from file: \n")
sp.pprint(M)
print("\n")

# do smth with matrix

print("Example 1: \t R1 = M + a * I : \n")
R1 = M + a * sp.eye(M.shape[0])
sp.pprint(R1)
print("\n")

print("Example 2: \t R2 = M + lamda * I : \n")
R2 = M + lamda * sp.eye(M.shape[0])
sp.pprint(R2)
print("\n")

print("Example 3: \t R3 = M - d * I : \n")
R3 = M - d * sp.eye(M.shape[0])
sp.pprint(R3)
print("\n")



