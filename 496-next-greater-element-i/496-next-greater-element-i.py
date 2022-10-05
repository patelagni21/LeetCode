class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        dic = {}
        
        for n in nums2:
            
            while stack and n > stack[-1]:
                dic[stack.pop()] = n
            stack.append(n)
            
        while stack:
            dic[stack.pop()] = -1
            
        for n in nums1:
            ans.append(dic[n])

        return ans        