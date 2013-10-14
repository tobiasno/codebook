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
	print generateBook( 100, 4 ); # Change the size of the book here

## Maps a given integer to a letter from the latin alphabet.
def mapIntToString( i ):
	if( i < 1 or i > 26 ):
		return "Error";
	return str( unichr( 64 + i ) );

printIt();
