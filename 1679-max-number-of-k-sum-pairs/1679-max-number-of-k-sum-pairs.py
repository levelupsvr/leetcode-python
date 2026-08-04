class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left<right:
            new=k-nums[left]
            if nums[right]==new:
                count+=1
                left+=1
                right-=1
            elif nums[right]<new:
                left+=1
            else:
                right-=1
        return count