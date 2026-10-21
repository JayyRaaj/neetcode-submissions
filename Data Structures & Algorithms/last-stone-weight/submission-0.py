import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            first = stones.pop()    # heaviest stone
            second = stones.pop()   # second heaviest stone
            
            if first != second:
                # Re-insert the remaining weight into the sorted list
                bisect.insort(stones, first - second)
                
        return stones[0] if stones else 0