class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i, n in enumerate(nums):
            key = target - n
            if key in map:
                return [map[key], i]
            map[n] = i
        