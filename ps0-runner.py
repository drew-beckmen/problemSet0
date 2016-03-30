#0 Test Cases:
from ps0 import is_even 
print("When asked if 0 is even, the answer is {}" .format(is_even(0)))
print("When asked if 4 is even, the answer is {}" .format(is_even(4)))
print("When asked if 5 is even, the answer is {}" .format(is_even(5)))


#1 Test Cases:
from ps0 import number_digits
print("The number 0 has {} digits." .format(number_digits(0)))
print("The number 12 has {} digits." .format(number_digits(12)))
print("The number 115 has {} digits." .format(number_digits(115)))


#2 Test Cases: 
from ps0 import sum_digits
print("The sum of the digits of 0 is {}." .format(sum_digits(0)))
print("The sum of the digits of 12 is {}." .format(sum_digits(12)))
print("The sum of the digits of 93 is {}." .format(sum_digits(93)))


#3 Test Cases:
from ps0 import sum_less_ints
print("The sum of the integers less than 4 is {}." .format(sum_less_ints(4)))
print("The sum of the integers less than 0 is {}." .format(sum_less_ints(0)))
print("The sum of the integers less than 1 is {}." .format(sum_less_ints(1)))
print("The sum of the integers less than 12 is {}." .format(sum_less_ints(12)))


#4 Test Cases:
from ps0 import factorial
print("The factorial of 0 is {}." .format(factorial(0)))
print("The factorial of 1 is {}." .format(factorial(1)))
print("The factorial of 5 is {}." .format(factorial(5)))
print("The factorial of 12 is {}." .format(factorial(12)))

#5 Test Case:
from ps0 import is_factor
print("When asked if 1 is a factor of 7, the answer is {}." .format(is_factor(7, 1)))
print("When asked if 2 is a factor of 4, the answer is {}." .format(is_factor(4, 2)))
print("When asked if 5 is a factor of 9, the answer is {}." .format(is_factor(9, 5)))
print("When asked if 3 is a factor of 12, the answer is {}." .format(is_factor(12, 3)))


#6 Test Case: 
from ps0 import is_prime
print("When asked if 2 is prime, the answer is {}." .format(is_prime(2)))
print("When asked if 3 is prime, the answer is {}." .format(is_prime(3)))
print("When asked if 4 is prime, the answer is {}." .format(is_prime(4)))


#7 Test Case: 
from ps0 import is_perfect
print("When asked if 6 is perfect, the answer is {}." .format(is_perfect(6)))
print("When asked if 27 is perfect, the answer is {}." .format(is_perfect(27)))
print("When asked if 28 is perfect, the answer is {}." .format(is_perfect(28)))


#8 Test Case: 
from ps0 import divided_by_sum_digits
print("When asked if the sum of the digits of 3 divides equally into 3, the answer is {}." .format(divided_by_sum_digits(3)))
print("When asked if the sum of the digits of 112 divides equally into 112, the answer is {}." .format(divided_by_sum_digits(112)))
print("When asked if the sum of the digits of 113 divides equally into 113, the answer is {}." .format(divided_by_sum_digits(113)))
