
'''Time Complexity: O(n)
    Space Complexity: O(n)
    Approach : I uses set method that basically only unique elements'''


def remove_duplicate(arr):
    seen = set()
    result = []

    for num in arr:
        if num  not in seen:
            seen.add(num)
            result.append(num)
    return result        

arr = [3,4,1,5,6,7,3,9,1]    
print(remove_duplicate(arr))        