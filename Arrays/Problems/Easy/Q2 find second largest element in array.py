"""
Problem: Find Second Largest Element in array
Platform: TUF
Time Complexity: O(n)
Space Complexity: O(1)
"""
arr = [8,5,9,1,3,6]
largest_element = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest_element:
        second_largest = largest_element
        largest_element = num

    elif num > second_largest and num != largest_element :
        second_largest = num
    print("second largest :" , second_largest)      