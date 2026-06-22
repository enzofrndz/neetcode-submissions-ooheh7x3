class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            hMap[tuple(count)].append(i)
        return list(hMap.values())
        