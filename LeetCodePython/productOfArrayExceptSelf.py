class Solution:
    def productExceptSelf(self, nums):
        #Initialize a pre and post variable 
        pre, post = 1, 1

        #Initialize an array of 1s of length: len(nums)
        output = [1 for _ in range(len(nums))]

        #Prefix iteration
        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]
      
        #Postfix iteration
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        return output
        
soln = Solution()
print(soln.productExceptSelf([1, 2, 3, 4]))
print(soln.productExceptSelf([-1,1,0,-3,3]))