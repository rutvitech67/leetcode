class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        first_seen = {}
        max_len = -1

        for i, ch in enumerate(s):
            if ch in first_seen:
                max_len = max(max_len, i - first_seen[ch] - 1)
            else:
                first_seen[ch] = i

        return max_len
