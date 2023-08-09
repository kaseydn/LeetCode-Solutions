class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        #Use a set to extract uniques from nums
        _nums = set(nums)
        
        #Iterate through set
        for num in _nums:
            #Check if it's the beginning of a sequence, otherwise move on
            if num - 1 not in _nums:
                curr = num + 1
                _longest = 1
                while curr in _nums:
                    curr += 1
                    _longest += 1
                    
                #Make comparison every round
                longest = max(longest, _longest)
        return longest
            

soln = Solution()
print(soln.longestConsecutive([100, 4, 200, 1, 3, 2]))
    