## Just another generator for One-Time-Pad codebooks
## this generator produces codebooks of variable size
## for the hand-use of OTP encryption.

## The quality of the random letters may vary with OS
## and available entropy.
## WARNING: Use in real situations is not recommended!

from __future__ import division
import math
import random

## System Generator
## Uses /dev/urandom or Windows CryptGenRandom
##
## Generates pseudo-random numbers which can be considered
## sufficient for cryptographic purposes.
##
## /dev/random will produce better results but can run
## out of entropy quickly.
## Always check the available entropy on your system.
## Linux: cat /proc/sys/kernel/random/entropy_avail
randObject = random.SystemRandom();

## Generates a block of five random latin letters and
## returns them as string.
def generateBlock():
	result = "";
	for i in range( 5 ):
		randNumber = randObject.randint( 1, 26 );
		letter = mapIntToString( randNumber );
		result += letter;
	return result;

## Generates a codebook of the given size and returns
## it as String.
def generateBook( n, columns ):
	result = "";
	for i in range( n ):
		if( i % columns == 0 ):
			result += "\n"
		result += generateBlock();
		result += " ";
	return result;

## Prints the output
def printIt():
	print generateBook(100, 4); # Change the size of the book here

## Maps a given integer to a letter from the latin alphabet.
def mapIntToString(i):
	if( i == 1 ):
		return "A";
	elif( i == 2 ):
		return "B";
	elif( i == 3 ):
		return "C";
	elif( i == 4 ):
		return "D";
	elif( i == 5 ):
		return "E";
	elif( i == 6 ):
		return "F";
	elif( i == 7 ):
		return "G";
	elif( i == 8 ):
		return "H";
	elif( i == 9 ):
		return "I";
	elif( i == 10 ):
		return "J";
	elif( i == 11 ):
		return "K";
	elif( i == 12 ):
		return "L";
	elif( i == 13 ):
		return "M";
	elif( i == 14 ):
		return "N";
	elif( i == 15 ):
		return "O";
	elif( i == 16 ):
		return "P";
	elif( i == 17 ):
		return "Q";
	elif( i == 18 ):
		return "R";
	elif( i == 19 ):
		return "S";
	elif( i == 20 ):
		return "T";
	elif( i == 21 ):
		return "U";
	elif( i == 22 ):
		return "V";
	elif( i == 23 ):
		return "W";
	elif( i == 24 ):
		return "X";
	elif( i == 25 ):
		return "Y";
	elif( i == 26 ):
		return "Z";
	else:
		return "Error";

printIt();
