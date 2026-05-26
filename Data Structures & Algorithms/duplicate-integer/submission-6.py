class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempnums=set(nums)
        if len(nums)==len(tempnums):
            return False
        return True