class Solution(object):
    def maximumDifference(self, nums):
        min_val = nums[0]
        ans = -1
        for num in nums[1:]:
            if num > min_val:
                ans = max(ans, num - min_val)

            min_val = min(min_val, num)

        return ans