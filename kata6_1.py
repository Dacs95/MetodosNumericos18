'''
Return the Factorial
Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
Examples
3 ➞ 6

5 ➞ 120

13 ➞ 6227020800
'''
def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)
