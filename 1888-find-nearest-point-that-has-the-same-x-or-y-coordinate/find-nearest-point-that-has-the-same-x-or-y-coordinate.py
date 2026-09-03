class Solution(object):
    def nearestValidPoint(self, x, y, points):
        minDist = float('inf')
        index = -1
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dist = abs(x - px) + abs(y - py)
                if dist < minDist:
                    minDist = dist
                    index = i

        return index
