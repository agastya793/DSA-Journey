
''' problem: rotate array by k position
    approach: brute force
    time complexity: O(n*k)'''


arr = [1,2,3,4,5,6,7]
k = 3

n = len(arr)

for _ in range(k):
    last = arr[-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = last

print(arr)     


#

# time complexity: O(n)
# space complexity: O(1)


def rotate(arr, k):
    n = len(arr)
    k = k % n

    arr.reverse()

    arr[:k] = reversed(arr[:k])

    arr[k:] = reversed(arr[k:])

    return arr


arr = [1,2,3,4,5,6,7]
k = 3

print(rotate(arr,k))