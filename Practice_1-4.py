'''Given a string, return the first character that appears only once.

Input:  "swiss"
Output: "w"

If no such character exists, return None.'''



text = 'swiss'

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print(char)
        break
    else:
        print('None') 

'''Given a list of integers, remove duplicates while maintaining the original order.

Input:  [4, 2, 4, 1, 2, 7, 1]
Output: [4, 2, 1, 7]

Constraint: Don't use set() directly for the final solution.'''


inputs =  [4, 2, 4, 1, 2, 7, 1]

unique_value_list = []

for num in inputs:
    if num not in unique_value_list:
        unique_value_list.append(num)

print(unique_value_list)


'''Given a string, return a dictionary containing the frequency of every character.

Input:  "programming"
Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, ...}

Ignore spaces and treat uppercase/lowercase as the same.'''

text = 'programming'

result = {}

for char in text.lower():
    if result != '':
        result[char] = result.get(char, 0) + 1

print(result)

'''Find the second-largest unique number in a list.

Input:  [10, 5, 20, 20, 8, 10, 15]
Output: 15

If there aren't at least two unique values, return None.'''

inputx = [10, 5, 20, 20, 8, 10, 15]
unique_inputx = []
largestx = none

resultx = None

for num in inputx:
    if num not in unique_inputx:
        unique_inputx.append(num)

for num in unique_inputx:
    
   