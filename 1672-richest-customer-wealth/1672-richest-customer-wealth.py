class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        
        for i in accounts:
            curr = sum(i)
            most = max(most, curr)
            
        return most