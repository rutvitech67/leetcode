class Solution:
    def isPalindrome(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                  return False
            left += 1
            right -= 1
        return True