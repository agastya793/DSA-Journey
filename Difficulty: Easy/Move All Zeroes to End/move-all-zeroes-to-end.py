class Solution:
	def pushZerosToEnd(self, arr):
    	non_zero_idx = 0
    	
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        arr[non_zero_idx], arr[i] = arr[i],arr[non_zero_idx]
    	        non_zero_idx += 1
    	