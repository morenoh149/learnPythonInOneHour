import random
import sys
import os

def addNumber(fNum, lNum):
	sumNum = fNum + lNum
	return sumNum

print(addNumber(1, 4))
string = addNumber(1, 4)

# print(sumNum)  # throws error, sumNum out of scope

print('What is your name')

name = sys.stdin.readline()

print('Hello ', name)  # computer is talking to you!


long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])
