class Solution:
        def shuffle(self, nums: List[int], n: int) -> List[int]:
                left = 0 
                right = len(nums) // 2
                result = []
                
                while left < len(nums) // 2 and right < len(nums):
                        result.append(nums[left])
                        left += 1
                        
                        result.append(nums[right])
                        right += 1            
                return result