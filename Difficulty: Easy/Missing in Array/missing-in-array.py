class Solution:
    def missingNum(self,arr):
        n= len(arr) + 1
        xor = 0
        
        for i in range(1, n+1):
            xor ^= i
            
        for num in arr:
            xor ^= num
        
        return xor    