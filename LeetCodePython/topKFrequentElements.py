from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        output = []

        #Generate a frequency cache using Counter
        counter = Counter(nums)

        #Declare an array of len(nums) + 1 spaces
        buckets = [[] for _ in range(len(nums) + 1)]

        #Iterate through the cache and fill buckets
        for num, count in counter.items():
            buckets[count].append(num)

        #Iterate backward through buckets
        for bucket in reversed(buckets):
            for v in bucket:
                output.append(v)
                #Return output once output == k
                if len(output) == k:
                    return output