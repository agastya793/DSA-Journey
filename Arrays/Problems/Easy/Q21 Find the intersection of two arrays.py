'''problem: Find the intersection of two arrays
   approach: 
   time complexity: O(n+m)
   space complexity : O(n)'''


arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

set1 = set(arr1)

result = []

for num in arr2:
    if num in set1:
        result.append(num)

print(result)



# Two pointer approach

def intersection(arr1, arr2):

    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            i += 1

        elif arr1[i] > arr2[j]:
            j += 1

        else:
            result.append(arr1[i])
            i += 1
            j += 1

    return result


arr1 = [1,2,3,4,5]
arr2 = [2,3,5,7]

print(intersection(arr1, arr2))