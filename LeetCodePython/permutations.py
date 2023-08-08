class Solution:
    def permute(self, nums):
        perms = []
        def generatePerm(index, nums):
            if index == len(nums):
                perms.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                generatePerm(index + 1, nums)
                nums[index], nums[i] = nums[i], nums[index]
        generatePerm(0, nums)        
        return perms
soln = Solution()
print(soln.permute([1, 2]))