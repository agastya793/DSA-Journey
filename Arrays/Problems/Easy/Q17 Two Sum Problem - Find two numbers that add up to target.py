'''problem : find two numbers that add up to target
   Approach: Brute force
   time  complexity: O(n^2)
    '''

'''Logic :

Pick first number

Compare it with every other number

If sum = target → return indices'''

arr = [1,5,6,7,8,9,10]

target = 10

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(i,j)

            #another approach 

#Instead of checking every pair, we store numbers we have already seen and quickly check if the required number exists.

'''approach: hashmap
  time complexity: O(n)
  space complexity: O(n) '''


arr = [6,4,6,7,8,9,2,4]  
target =  13

hashmap = {}

for i,num in enumerate(arr):
    needed = target - num

    if needed in hashmap:
        print(hashmap[needed],i)
        break

    hashmap[num] = i

