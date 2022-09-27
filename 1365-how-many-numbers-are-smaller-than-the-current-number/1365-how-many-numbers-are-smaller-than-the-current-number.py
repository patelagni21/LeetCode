class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter, arr = 0, []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            arr.append(counter)
            counter = 0
        
        return arr
                
            
            