# Hashset approach
class Solution:
    def removeDuplicate(self, arr):
        seen = set()
        result = []
        
        for x in arr:
            if x not in seen:
                seen.add(x)
                result.append(x)
        return result       
        

