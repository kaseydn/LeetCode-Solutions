class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] < target:
                l += 1
            elif nums[m] > target:
                r -= 1
            else:
                return m

soln = Solution()
print(soln.search([-1,0,3,4,5,9,12], 9)) # 4
        