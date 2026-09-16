class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum=nums[0]
        current=0
        for i in nums:
            current+=i
            max_sum=max(max_sum,current)
            if current<0:
                current=0
        return max_sum