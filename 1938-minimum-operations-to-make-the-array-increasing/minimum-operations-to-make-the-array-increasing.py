class Solution(object):
    def minOperations(self, nums):
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] - nums[i] + 1
                operations += diff
                nums[i] += diff  
        return operations
