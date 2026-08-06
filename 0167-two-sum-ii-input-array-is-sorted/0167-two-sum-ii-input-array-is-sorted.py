class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            k=target-numbers[left]
            if numbers[right]==k and left<right:
                return [left+1,right+1]
            elif k>numbers[right] :
                left+=1
            else:
                right-=1
            
        