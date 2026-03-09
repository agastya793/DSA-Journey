'''problem : find average of array elements
   time  complexity: O(n)
   space complexity: O(1) '''



arr = [1,23,3,4,5,6]
total_sum = 0
for num in arr:
    total_sum += num
    average = total_sum / len(arr)
print("average of array elements are:",average)    
