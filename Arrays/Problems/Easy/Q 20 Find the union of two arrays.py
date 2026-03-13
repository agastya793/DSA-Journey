'''problem: find union of two arrays
   approach: set + loop
    time complexity: O(n+m)
    space complexity: O(n+m)'''


def union_arrays(arr1,arr2):
    union = set()

    for num in arr1:
        union.add(num)

    for num in arr2:
        union.add(num)    

    return union
    
arr1 = [1,2,3,4,5,6]  
arr2 = [2,6,7,8,9,2] 

print(union_arrays(arr1,arr2))



