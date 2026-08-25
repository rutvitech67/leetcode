class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        drank = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_full = empty // numExchange
            drank += new_full
            empty = empty - new_full * numExchange + new_full
        return drank
