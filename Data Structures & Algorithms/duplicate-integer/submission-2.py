class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listNums = []
        for i in nums:
            if i in listNums:
                return True
            listNums.append(i)
        return False

        


        