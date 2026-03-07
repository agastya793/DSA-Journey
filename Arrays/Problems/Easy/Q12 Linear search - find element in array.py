'''problem: find element in array
   Time complexity: BEST CASE- O(1) , worst case- O(n)
   space complexity: O(1)'''

#Linear search means checking each element one by one until you find the target element.
'''Use it when:

Data is unsorted

Array size is small'''

# using linear search
arr = [3,45,8,9,2,1]
target = 1
for i in range(len(arr)):
    if arr[i] == target:
        print("element found at index:",i)
        break


# using function

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [4,6,7,3,2,9]    
target = 2

result = linear_search(arr,target)

if result != -1 :
    print("element found at index:",result)
else: 
    print("element not found")    

