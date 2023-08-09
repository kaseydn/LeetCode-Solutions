class Solution:
    def dailyTemperatures(self, temperatures):
        #Generate an array of len(temperatures) - 1 spaces
        output = [0 for _ in range(len(temperatures))]
        #Init a stack
        stack = []
        #Iterate through temperatures
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                output[index] = i - index 
            stack.append((t, i))
        return output
temperatures = [50, 40, 30]
soln = Solution()
print(soln.dailyTemperatures(temperatures)) # [0, 0, 0]
