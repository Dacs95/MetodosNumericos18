'''
Create a function that takes a list of numbers and returns the following statistics:
Minimum Value
Maximum Value
Sequence Length
Average Value
Examples
[6, 9, 15, -2, 92, 11] ➞ [-2, 92, 6, 21.833333333333332]

[30, 43, 20, 92, 3, 74] ➞ [3, 92, 6, 43.666666666666664]

[4.54, 8.32, 5.20] ➞ [4.54, 8.32, 3, 6.02]
'''
def minMaxLengthAverage(lst):
	suma = sum(lst)
	avg= suma/len(lst)
	newLst = [min(lst), max(lst), len(lst),avg]
	return newLst
