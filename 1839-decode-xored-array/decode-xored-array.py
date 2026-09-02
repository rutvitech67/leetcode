class Solution(object):
    def decode(self, encoded, first):
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        for i in range(len(encoded)):
            arr[i+1] = arr[i] ^ encoded[i]

        return arr
