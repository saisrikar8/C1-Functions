'''
04/15/2021

Functions:
A function is a group of related statements that performs a specific task.

Functions help us breakdown our program into sections.

DRY: Don't Repeat Yourself

Formula for functions:
def FUNCTIONNAME(OPTIONAL PARAMETERS):
	BODY including optional return statements

To use a function, we have to call it:
FUNCTIONNAME(OPTIONAL PARAMETERS)

'''

# get name function
'''
def getName():
	userName = input("Please tell me your name:\n")
	return userName

def greeting(name):
	print("Hi " + name)

name1 = getName()
greeting(name1)

name2 = getName()
greeting(name2)

name3 = getName()
greeting(name3)
__________________________________________________

Ask the user for two numbers
num1
num2

Write a function that takes num1 and num2 as PARAMETERS

print the sum

'''
def sumOfNums(numList):
	total = 0
	for i in numList:
		total += i
	print("The sum is " + str(total))
sumOfNums([1,2,3,4,5,6,7,8,9,10])

def productOfNums(numList):
	total = 1
	for i in numList:
		total *= i
	print("The product is " + str(total))
sumOfNums([1,2,3,4,5,6,7,8,9,10])
productOfNums([1,2,3,4,5,6,7,8,9,10])