class Solution:
    def isPalindrome(self, s):
        #Two pointer solution
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True