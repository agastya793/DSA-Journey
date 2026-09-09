class Solution:
    def twoSum(self, arr, target):
        seen = {}

        for i in range(len(arr)):
            complement = target - arr[i]

            if complement in seen:
                return True

            seen[arr[i]] = i

        return False