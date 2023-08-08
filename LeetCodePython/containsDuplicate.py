class Solution:
    def containsDuplicate(self, nums):
        numbers = set()
        for n in nums:
            if n in numbers:
                return True
            numbers.add(n)
        return False