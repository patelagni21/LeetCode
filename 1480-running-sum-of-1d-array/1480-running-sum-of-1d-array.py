class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            arr.append(count)
        return arr
                