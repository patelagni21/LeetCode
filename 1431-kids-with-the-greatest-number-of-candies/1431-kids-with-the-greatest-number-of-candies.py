class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        for i in range(len(candies)):
            arr.append(candies[i] + extraCandies >= max(candies))
            
        return arr
