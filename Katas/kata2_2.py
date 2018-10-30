'''
Create a function that takes a list of non-negative numbers / strings and returns a new list without the strings.
Example
[1, 2, "a", "b"] ➞ [1, 2]

[1, "a", "b", 0, 15] ➞ [1, 0, 15]

[1, 2, "aasf", "1", "123", 123] ➞ [1, 2, 123]
'''
def filter_list(lst):
	nlst = list()
	for i in lst:
		if isinstance(i,int):
			nlst.append(i)
	return nlst
