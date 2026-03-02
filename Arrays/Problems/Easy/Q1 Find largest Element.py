"""
Problem: Find Largest Element
Platform: TUF
Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [8,6,9,5,7]
max_element = arr[0]
for i in range(len (arr)):
    if arr[i] > max_element:
        max_element = arr[i]
        print(max_element)
    