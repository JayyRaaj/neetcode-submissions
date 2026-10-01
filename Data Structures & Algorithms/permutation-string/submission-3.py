class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for l in range(0, len(s2)-len(s1)+1):
            word = ""
            for i in range(0, len(s1)):
                word = word + s2[l+i]
            
            if sorted(s1) == sorted(word):
                return True            
        
        return False
