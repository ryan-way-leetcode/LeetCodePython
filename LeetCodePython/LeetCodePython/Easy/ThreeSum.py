class Solution:
    def threeSum(self, nums):
        nums.sort()
        
        check = {}
        for i in nums:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1

        retVal = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue

            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]: continue

                complete = 0-nums[i]-nums[j]
                if complete not in check: continue
                if complete < nums[i] or complete < nums[j]: continue
                if complete == nums[i] and check[complete] < 2: continue
                if complete == nums[j] and check[complete] < 2: continue
                if complete == nums[i] and complete == nums[j] and check[complete] < 3: continue

                retVal.append([nums[i], nums[j], complete])

        return retVal