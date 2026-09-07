class Solution:
    def findMean(self, arr):
        total = 0
        
        for num in arr:
            total += num
            
        return total //  len(arr)
        