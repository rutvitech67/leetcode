class Solution(object):
    def destCity(self, paths):
        starts = set()
        for a, b in paths:
            starts.add(a)       # collect all starting cities
        for a, b in paths:
            if b not in starts: # destination city has no outgoing path
                return b
