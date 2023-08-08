class Solution:
    def checkInclusion(self, s1, s2):
        #Make a char array for each string
        a1, a2 = [0] * 26, [0] * 26

        #Populate a1 and a2
        for i, c in enumerate(s1):
            a1[ord(c) - ord('a')] += 1
            a2[ord(s2[i]) - ord('a')] += 1
        
        #Sliding window algo
        
        return a1 == a2