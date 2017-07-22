## Just another generator for One-Time-Pad codebooks
## this generator produces codebooks of variable size
## for the hand-use of OTP encryption.

## The quality of the random letters may vary with OS
## and available entropy.
## WARNING: Use in real situations is not recommended!

import string
import secrets

## Now implemented with python's secrets library and
## therefor should use the best source of entropy on
## the system.
##
## Requires at least Python3.6
## 
## Generates pseudo-random numbers which can be considered
## sufficient for cryptographic purposes.
##
## Always check the available entropy on your system.
## Linux: cat /proc/sys/kernel/random/entropy_avail

## Generates a block of five random latin letters and
## returns them as string.
def generateBlock():
    alphabet = string.ascii_uppercase
    result = ""
    for i in range(5):
        result += secrets.choice(alphabet)
    return result

## Generates a codebook of the given size and returns
## it as String.
def generateBook(n, columns):
    result = ""
    for i in range(n):
        if(i % columns == 0):
            result += "\n"
        result += generateBlock()
        result += " "
    return result

## Prints the output
def printIt():
    print(generateBook(100, 4)) # Change the size of the book here

printIt()
