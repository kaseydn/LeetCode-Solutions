from collections import Counter
class Solution:
    def permuteUnique(self, nums):
        paths = []
        path = []
        def generatePath(cache):
            if len(path) == len(nums):
                paths.append(path[:])
                return
            for num in cache:
                if cache[num]:
                    cache[num] -= 1
                    path.append(num)
                    generatePath(cache)
                    path.pop()
                    cache[num] += 1
        generatePath(Counter(nums))
        return paths
    
soln = Solution()
print(soln.permuteUnique([1, 1, 2]))
        