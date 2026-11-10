class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateMap = dict()

        for x in range(len(nums)):
            if nums[x] in duplicateMap:
                return True
            duplicateMap[nums[x]] = True

        return False
