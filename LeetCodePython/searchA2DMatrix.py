class Solution:
    def searchMatrix(self, matrix, target):
        #Binary Search Rows
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                #Binary Search Columns
                row = matrix[m]
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] < target:
                        l += 1
                    elif row[mid] > target:
                        r -= 1
                    else:
                        return True
                return False
        return False

matrix = [[1]]
soln = Solution()
print(soln.searchMatrix(matrix, 2))