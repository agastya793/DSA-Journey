'''problem : find an element
   approach : linear search
   time  complexity: worst case- O(n), best case - O(1)
   space complexity: O(1)'''
# using linear search
arr = [2,4,5,6,7,9,2,3,4,5,6,]
target = 2
found = False

for num in arr:
    if num == target:
       found = True
       break

if found:
    print("element exist that is:",target)
else:
    print("element not found")    



    
