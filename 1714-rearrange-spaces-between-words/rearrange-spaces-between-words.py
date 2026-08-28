class Solution(object):
    def reorderSpaces(self, text):
        space_count = text.count(" ")
        words = text.split()
        word_count = len(words)
        
        if word_count == 1:
            return words[0] + " " * space_count
        
        between = space_count // (word_count - 1)
        extra = space_count % (word_count - 1)
        
        return (" " * between).join(words) + " " * extra
