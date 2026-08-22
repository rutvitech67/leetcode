class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)   # Step 1: find current max
        result = []
        for c in candies:           # Step 2: check each kid
            result.append(c + extraCandies >= maxCandies)
        return result
