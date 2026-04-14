class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = {}
        hashTable2 = {}
        for char in s:
            if char not in hashTable:
                hashTable[char] = 1
            else:
                hashTable[char] += 1

        for char in t:
            if char not in hashTable2:
                hashTable2[char] = 1
            else:
                hashTable2[char] += 1

        if hashTable == hashTable2:
            return True
        return False
        
        