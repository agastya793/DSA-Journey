'''problem: find all pairs with given sum
Approach: Brute force
time complexity: O(n^2)'''
arr = [2,4,5,6,7,8,-1]
target = 13

for i in range(len(arr)):
    for j in range(i + 1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])
            

            # using hashmap

'''time complexity : O(n)'''
arr = [3,5,6,7,8,8,2,1]   
target =   10   

seen = {}

for num in arr:
    needed = target - num

    if needed in seen:
        print(needed,num)

    seen[num] = True