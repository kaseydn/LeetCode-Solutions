class Solution:
    def twoSum(self, numbers, target):
        #Two pointer solution
        l, r = 0, len(numbers) - 1
        while l < r:
            _twoSum = numbers[l] + numbers[r]
            if _twoSum > target:
                r -= 1
            elif _twoSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        