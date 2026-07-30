class Solution(object):
    def generate(self, numRows):
        triangle = []

        for row in range(numRows):
            # Start each row with 1s
            new_row = [1] * (row + 1)

            # Fill in the middle values
            for j in range(1, row):
                new_row[j] = triangle[row-1][j-1] + triangle[row-1][j]

            triangle.append(new_row)

        return triangle
