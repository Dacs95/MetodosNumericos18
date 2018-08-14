'''
Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).
Examples
["John", "Taylor", "John"] ➞ ["John", "Taylor"]

[1, 0, 1, 0] ➞ [1, 0]

['The', 'big', 'cat'] ➞ ['The', 'big', 'cat']
'''
def removeDups(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
