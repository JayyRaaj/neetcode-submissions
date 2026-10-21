import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        # Binary search insert to keep self.nums sorted: O(n)
        bisect.insort(self.nums, val)
        
        # The kth largest element is at index -k
        return self.nums[-self.k]