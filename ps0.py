#0. Even or odd function
def is_even(number):
	"""Will return True if a non-negative number is even and false if the number is odd"""
	number = int(number)
	test = number % 2 #remainder when divided by 2
	if test > 0: #if remainder when divided by 2, the number must be odd (or False b/c not even)
		return False
	else:
		return True

#1. Number digits in integer
def number_digits(number):
	"""Will return the number of digits in a non-negative integer"""
	number = str(number) #convert to string to use len function
	numberOfDigits = len(number)
	return numberOfDigits
	
#2. Sum of digits in integer
def sum_digits(number):
	"""Will return the sum of the digits of a non-negative integer"""
	number = str(number)
	lengthOfNumber = len(number)
	listDigits = []
	index = 0
	while index <= lengthOfNumber-1: #don't forget -1 b/c index starts at 0
		numberAppending = number[index] #you can use indexes for strings
		numberAppending = int(numberAppending) #convert number to int before adding to list so can be added together
		listDigits.append(numberAppending)
		index += 1
	finalAnswer = sum(listDigits) #used sum function to add all int contents of the list 
	return finalAnswer

#3. Sum of integers < given number #found range function here: https://docs.python.org/2/library/functions.html#range
def sum_less_ints(number):
	"""Will return the sum of all integers less than the given integer"""
	number = int(number)
	listOfInts = range(1, number) #range creates list but doesn't include the number
	sumLessInts = sum(listOfInts) #sum function adds all contents of list together
	return sumLessInts

#4. Factorial of number
def factorial(number):
	"""Will return the factorial of a non-negative number"""
	number = int(number)
	listOfInts = range(1, number + 1) #add plus one because range is up to but not including 
	product = 1 #no special case for 0 needed. 0! = 1
	for item in listOfInts:
		product *= item #multiple all contents of list together
	return product

#5. Finds if number is factor of other number
def is_factor(dividend, divisor):
	"""Will return True if positive number is a factor of the other positive number, and False if not a factor"""
	dividend = int(dividend)
	divisor = int(divisor)
	test = dividend % divisor
	if test > 0: #if there is a remainder then the numbers don't divide evenly
		return False
	else:
		return True
#6. Finds if number is prime
def is_prime(number):
	"""Will return False if positive number is not prime, and True if the number is prime"""
	number = int(number) 
	listPossibleDivisors = range(2, number) #all possible numbers that could be divided and make number not prime
	for item in listPossibleDivisors:
		if number % item == 0: 
			return False #returns False if not prime 
	return True

#7. Finds if number is perfect
def is_perfect(number):
	"""Will return True if the positive integer is perfect, and False if the number is not"""
	number = int(number)
	listFactors = []
	listPossibleDivisors = range(1, number) #factor can't be the number itself
	for item in listPossibleDivisors:
		if number % item == 0:
			listFactors.append(item) #add that factor to the list of factors
	sumOfFactors = sum(listFactors) #add up all factors
	if sumOfFactors == number: #only if all factors are = to the number is it perfect
		return True
	else:
		return False

#8. Finds if number and sum of digits of number divides evenly
from ps0 import sum_digits
def divided_by_sum_digits(number):
	"""Will return True if sum of digits of a positive number can be divided equally into the number, otherwise returns False"""
	result = sum_digits(number) #calling sum_digits function
	number = int(number)
	test = number % result
	if test == 0: #if no remainder, then the numbers divide evenly
		return True
	else: 
		return False