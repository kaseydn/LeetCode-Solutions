class Solution:
    def characterReplacement(self, s, k):
        cache = {}
        l = 0
        major = 0
        for r, c in enumerate(s):
            cache[c] = cache.get(c, 0) + 1
            major = max(major, cache[c])
            if r - l + 1 - major > k:
                cache[s[l]] -= 1
                l += 1
        return r - l + 1