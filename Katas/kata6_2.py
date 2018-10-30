'''
Daniel Contreras
Absolutely Sum
Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
Examples
[2, -1, 4, 8, 10] ➞ 25

[-3, -4, -10, -2, -3] ➞ 22

[2, 4, 6, 8, 10] ➞ 30

[-1] ➞ 1
'''


def get_abs_sum(lst):
	sum = 0
	for i in range(len(lst)):
		sum = abs(lst[i]) + sum
	return sum
