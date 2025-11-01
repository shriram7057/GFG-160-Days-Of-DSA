import heapq

class Solution:
    def kLargest(self, arr, k):
        return heapq.nlargest(k, arr)
