class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Place all non-positive numbers out of the way
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1

        # Step 2: Mark presence using index
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                if arr[val - 1] > 0:
                    arr[val - 1] = -arr[val - 1]

        # Step 3: Find first positive index
        for i in range(n):
            if arr[i] > 0:
                return i + 1

        return n + 1
