"""
Approach: Two Pointer-Swap elements from start and end moving toward the center.
Problem: Reverse an array
Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [2,3,5,7,8,1,2,9]

start = 0
end = len(arr)-1

while start < end :
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
print(arr)    