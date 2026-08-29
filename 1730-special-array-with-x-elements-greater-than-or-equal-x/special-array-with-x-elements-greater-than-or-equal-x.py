class Solution(object):
    def specialArray(self, nums):
        n = len(nums)
        nums.sort()

        for x in range(1, n+1):
            count = sum(1 for num in nums if num >= x)
            if count == x:
                return x

        return -1
