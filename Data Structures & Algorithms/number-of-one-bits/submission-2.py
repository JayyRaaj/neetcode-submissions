class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n != 0:
            c = n % 2
            if c == 1:
                counter += 1
            n = n // 2

        return counter