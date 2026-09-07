class Solution:
    def countFreq(self, arr):
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            
            else:
                freq[num] = 1
              
        
        res = []
        for num in freq:
            res.append([num,freq[num]])
        return res    