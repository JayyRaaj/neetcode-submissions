class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        for i in range(32):
            out += (n >> i) & 1
        return out