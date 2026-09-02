class Solution(object):
    def countGoodRectangles(self, rectangles):
        maxLen = 0
        for l, w in rectangles:
            maxLen = max(maxLen, min(l, w))
        count = 0
        for l, w in rectangles:
            if min(l, w) == maxLen:
                count += 1

        return count
