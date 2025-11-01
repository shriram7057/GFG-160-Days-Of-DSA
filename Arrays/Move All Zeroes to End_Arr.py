class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        count = 0  # Position to place the next non-zero element

        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        # Fill remaining positions with zeroes
        while count < n:
            arr[count] = 0
            count += 1
