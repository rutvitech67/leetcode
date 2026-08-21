class Solution(object):
    def luckyNumbers(self, matrix):
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        return [num for num in row_min if num in col_max]
