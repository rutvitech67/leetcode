from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        freq = Counter(nums)
        count = 0
        for k in freq.values():
            count += k * (k - 1) // 2
        return count
