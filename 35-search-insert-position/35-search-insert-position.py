class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for idx in range(len(nums)):
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                return idx
        return len(nums)