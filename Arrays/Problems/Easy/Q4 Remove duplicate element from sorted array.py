'''problem : we need to remove duplicate element from sorted array
   time complexity : O(n)
   space complexity :O(1)
   Approach: I used the two-pointer technique — one pointer scans the array while the other tracks the position of unique elements.  
   '''

def remove_duplicate(arr):
    if not arr:
        return 0
    k = 0 
    for i in range(1,len(arr)):
        if arr[i] != arr[k]:
            k +=1
            arr[k] = arr[i]
    return k + 1

arr = [1,1,2,23,4,4,5,5,6,6,6,7,8,8,8,9,9]  
length = remove_duplicate(arr)  

print("New length:" , length )
print("unique element:", arr[:length])

