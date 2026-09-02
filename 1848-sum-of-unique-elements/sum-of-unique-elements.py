class Solution(object):
    def sumOfUnique(self, nums):
        total = 0
        for x in nums:
            if nums.count(x) == 1:   
                total += x
        return total
