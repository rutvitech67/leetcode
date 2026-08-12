from collections import Counter

class Solution(object):
    def commonChars(self, words):
        common = Counter(words[0])
        for w in words[1:]:
            common &= Counter(w)
        result = list(common.elements())
        return result
