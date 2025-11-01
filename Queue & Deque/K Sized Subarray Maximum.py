from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        dq = deque()
        result = []

        for i in range(n):
            # Remove elements out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements in k range as they are useless
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            # Append max in window to result
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
