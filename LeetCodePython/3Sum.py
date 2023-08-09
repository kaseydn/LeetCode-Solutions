class Solution:
    def threeSum(self, nums):
        output = []
        #Sort the array
        nums.sort()
        #Iterate through nums
        for i, a in enumerate(nums):
            #Check for duplicate nums
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #Implement a two pointer solution from twoSum2
            l, r = i + 1, len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                _threeSum = a + b + c
                if _threeSum < 0:
                    l += 1
                elif _threeSum > 0:
                    r -= 1
                else:
                    output.append([a, b, c])
                    l += 1
                    #Check for duplicate nums
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return output
soln = Solution()
print(soln.threeSum([0, 0, 0]))
        
        