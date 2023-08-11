class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, runningSum = float('-inf'), 0
        for i, n in enumerate(nums):
            if n > n + runningSum:
                runningSum = 0
            runningSum += n
            maxSum = max(maxSum, runningSum)
        return maxSum