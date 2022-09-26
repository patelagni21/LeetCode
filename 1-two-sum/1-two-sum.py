class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hasmap
        prevMap = {}  # val -> index
        #iterate through index and value in nums
        for i, n in enumerate(nums):
            # DIFFERENCE is the target integer - n  
            diff = target - n
            #checking if this difference is already in the hash map
            if diff in prevMap:
                #we want to return a pair of indeces
                #differnece is one index and i is the other
                return [prevMap[diff], i]
            #if we dont find solution, we want to keep going since we are GUARENTEED A SOL
            prevMap[n] = i