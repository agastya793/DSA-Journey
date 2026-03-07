
'''problem: Find missing number in array (1 to n)
   Approach: sum formula
   time complexity: O(n)
   space complexity:O(1) '''


arr = [1,2,4,5]

n = len(arr) + 1

expected_sum = n *( n+1 ) // 2
actual_sum = sum(arr)
missing_number = expected_sum - actual_sum
print("missing number:",missing_number)
