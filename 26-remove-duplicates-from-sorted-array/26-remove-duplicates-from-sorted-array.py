class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        #start at index one since index zero has to be a UNIQUE number which has obv not been repeated before
        for right in range(1, len(nums)):
            #is this value new or one that has alr been repeated....right-1 compares to the previous
            #so if it is not equal, then it is a new unique value
            if nums[right] != nums[right-1]:
                #since it is a new unique value we want to put the value at right pointer where the left pointer is
                #Left pointer tracks the places of unique values in the arr
                #right pointer tracks values in the array and if we find unique values, we want to add it to its appropriate place in the array
                nums[left] = nums[right]
                #increment Left pointer since we want to fill in the next number
                left += 1
        #Left pointer tracks the places of unique values so this would be the output!!!!
        return left
    #damn this was fun