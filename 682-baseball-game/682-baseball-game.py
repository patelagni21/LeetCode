class Solution:
    def calPoints(self, operations: List[str]) -> int:
        munch = []
        
        for i in operations:
            if i  == "+":
                munch.append(munch[-1] + munch[-2])
            
            elif i == "C":
                munch.pop()
            
            elif i == "D":
                munch.append(munch[-1]*2)
            
            else:
                munch.append(int(i)) #str list to a integer to add it
            
        return sum(munch)
            
                       
            
