"""
Problem: Find Smallest Element
Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [2,3,6,9,1,2,0,4]
smallest_element = arr[0]
for i in range(len(arr)):
    if arr[i] < smallest_element:
       smallest_element = arr[i]
print("smallest element:",smallest_element)    



