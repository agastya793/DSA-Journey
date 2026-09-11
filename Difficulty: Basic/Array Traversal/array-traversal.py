class Solution:
    def arrayTraversal(self,arr,n):
        for i in range (n):
            if i > 0:
                print(" ", end = "")
            print(arr[i], end = "")
        
        