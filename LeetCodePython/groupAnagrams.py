class Solution:
    def groupAnagrams(self, strs):
        #Construct a cache
        cache = {}

        #Iterate through the strings
        for s in strs:
            #Construct a key for each string
            key = ''.join(sorted(list(s)))
            #Create key if it doesn't exist
            if not key in cache:
                cache[key] = []
            #Append s to the value of the key
            cache[key].append(s)
        return cache.values()
    
soln = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(soln.groupAnagrams(strs))
  