class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash1, hash2 = {}, {}

        for n in s:
            if n in hash1:
                hash1[n] = hash1[n] + 1
            else:
                hash1[n] = 1
        for m in t:
            if m in hash2:
                hash2[m] = hash2[m] + 1
            else:
                hash2[m] = 1
        
        return hash1 == hash2
        