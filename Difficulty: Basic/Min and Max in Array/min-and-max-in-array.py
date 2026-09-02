class Solution:
    def getMinMax(self, arr):
        min_num = arr[0]
        max_num = arr[0]
        
        for num in arr[1:]:
            if num < min_num:
                min_num = num
            elif num > max_num:
                max_num = num 
                
        return min_num,max_num        
        