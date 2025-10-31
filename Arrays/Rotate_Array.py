class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # Handle cases where d > n
        arr[:] = arr[d:] + arr[:d]
