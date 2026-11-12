class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ''.join(char for char in s if char.isalnum())
        j = len(cleaned) - 1
        for i in range(len(cleaned)):
            first = cleaned[i].lower()
            last = cleaned[j].lower()
            if first != last:
                return False
            j = j - 1
        
        return True