class Solution:
    def generateParenthesis(self, n):
        # paths, path = [], []
        # def generatePath(left, right):
        #     if left == 0 == right:
        #         paths.append(''.join(path))
        #         return
        #     if left:
        #         path.append('(')
        #         generatePath(left - 1, right)
        #         path.pop()
        #     if right > left:
        #         path.append(')')
        #         generatePath(left, right - 1)
        #         path.pop()
        # generatePath(n, n)
        # return paths
        dp = [[] for i in range(3)]
        dp[0].append('')
        for i in range(3):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
soln = Solution()
print(soln.generateParenthesis(2)) # ['()()', '(())']
        