'''Problem : Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not.
If the array is sorted then return True, Else return False.

Platform: TUF
Time Complexity: O(n)
space complexity: O(1) '''

# This function checks if the array is sorted in ascending (non-decreasing) order

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = [34,45,67,54,34,87,20]
print(is_sorted(arr))
