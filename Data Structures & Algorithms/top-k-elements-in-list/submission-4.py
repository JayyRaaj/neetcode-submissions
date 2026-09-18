class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        # Count each number
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Sort numbers by their frequency
        sorted_nums = sorted(frequency, key=frequency.get, reverse=True)

        # Return first k numbers
        return sorted_nums[:k]
        