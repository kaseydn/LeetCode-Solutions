class Solution:
    def generateParenthesis(self, n):
        paths, path = [], []
        def generatePath(left, right):
            if left == 0 == right:
                paths.append(''.join(path))
                return
            if left:
                path.append('(')
                generatePath(left - 1, right)
                path.pop()
            if right > left:
                path.append(')')
                generatePath(left, right - 1)
                path.pop()
        generatePath(n, n)
        return paths
soln = Solution()
print(soln.generateParenthesis(2)) # ['()()', '(())']
print(soln.generateParenthesis(1)) # ['()']
print(soln.generateParenthesis(0)) # []
        