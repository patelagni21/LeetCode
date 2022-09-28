class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            value = nums[nums[i]]
            ans.append(value)
        return ans
            