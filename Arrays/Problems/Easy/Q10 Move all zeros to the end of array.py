'''problem : move all zeroes to the end of array
time complexity : O(n)
 space complexity: O(n)
 approach : Brute force'''

arr = [1,2,0,4,0,5,7,0,6]
new_arr = []
for num in arr:
    if num != 0:
        new_arr.append(num)
while len(new_arr) <  len(arr) :
    new_arr.append(0)
print(new_arr)    

# optimal method

'''Approach: Two pointer
   Time complexity:O(n)
    Space complexity:O(1)'''


arr = [1,7,0,9,45,5,7,0,6]
pos = 0  # position to place next non-zero element
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos],arr[i] = arr[i],arr[pos] 
        pos += 1
print(arr)        




