'''problem: count frequency of elements
   approach : using dictionary
   time complexity:O(n)
   space complexity:O(n) '''

arr = [1,2,2,3,1,4,2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num]  = 1
print(freq)        

# using enumerate
arr = [6,7,8,4,3,5,4,8,2]

target = 8

indices = []
count = 0
for i , val in enumerate(arr):
    if val == target:
       indices.append(i)
       count += 1
print("Indices:", indices)
print("Count:", count)