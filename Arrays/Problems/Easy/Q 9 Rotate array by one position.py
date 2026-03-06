'''problem : rotate array by one position
   time complexity:O(n)
   space complexity: O(1)
   left rotation method'''

arr = [1,2,3,45,6,7]
temp = arr[0]
for i in range(len(arr)-1):
    arr[i] = arr[i+1]
arr[len(arr)-1]  = temp

print(arr)

