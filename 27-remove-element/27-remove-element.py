class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        #k pointer starts at 0
        for i in range(len(nums)):
            if nums[i] != val:
                #nums at index i != value, then we want the value in the front of the line
                nums[k] = nums[i]
                #so we swap the value where k pointer is with the value where i pointer since we want it to be in the front
                k += 1
                #increment k pointer so we can move forward to the next
        return k
                #return k since we only want the number of elements that are non-duplicates