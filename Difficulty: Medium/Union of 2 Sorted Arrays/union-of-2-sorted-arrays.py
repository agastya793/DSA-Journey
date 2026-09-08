class Solution:
    def findUnion(self, a, b):
        i = 0
        j = 0
        result = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1

            elif a[i] > b[j]:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1

            else:
                # Both are equal
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1

        # Remaining elements of a
        while i < len(a):
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        # Remaining elements of b
        while j < len(b):
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result