class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        p = -1
        q = -1
        for i in range(len(nums)-2, 0,-1):
            if nums[i] < nums[i+1]:
                p = i
                break
        if p == -1: 
            nums = list(reversed(nums))
            return
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[p]:
                q = i
                break
        temp = nums[p]
        nums[p] = nums[q]
        nums[q] = temp
        nums[p+1:] = reversed(nums[p+1:])
        return nums

