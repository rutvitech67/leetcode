class Solution(object):
    def trimMean(self, arr):
        n = len(arr)
        remove = n // 20  
        arr.sort()
        trimmed = arr[remove : n - remove]  
        return sum(trimmed) / float(len(trimmed))
