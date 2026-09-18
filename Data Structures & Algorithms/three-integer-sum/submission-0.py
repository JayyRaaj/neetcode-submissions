class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        final = []
        nums.sort()
        for i in range(0, l-2):
            for j in range(i+1,l-1):
                for k in range(j+1, l):
                    if (nums[i]+nums[j]+nums[k]==0):
                        final.append([nums[i],nums[j],nums[k]])

        result = [list(t) for t in {tuple(sorted(t)) for t in final}]

        return result 
