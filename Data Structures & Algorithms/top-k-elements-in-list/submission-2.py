class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)

        arr = []
        for num, cnt in hashMap.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        