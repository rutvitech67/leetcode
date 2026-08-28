class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0

        for i, val in enumerate(arr):
            count = (i + 1) * (n - i)
            odd_count = (count + 1) // 2
            total += val * odd_count

        return total
