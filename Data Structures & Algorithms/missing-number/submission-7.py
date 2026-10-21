class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        print(length)
        if length > nums[-1]:
            max = length
        else:
            max = nums[-1]
        for i in range(0, max+1):
            if i not in nums:
                return i
            
        
        return 0