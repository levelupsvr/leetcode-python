class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        high=max(candies)
        for ch in candies:
            if high<=ch+extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        