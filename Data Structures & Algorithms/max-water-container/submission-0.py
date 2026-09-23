class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
            l = 0
            r = len(heights) - 1

            maximum = 0

            while ( l < r):
                area = min(heights[l],heights[r])*(r-l)
                if area > maximum:
                    maximum = area
                
                if heights[l] < heights[r]:
                    l = l + 1
                else:
                    r = r - 1

            return maximum
        