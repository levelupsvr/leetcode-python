class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        count = 0

        for i in range(1, len(nums)):
            count += nums[i] - nums[0]

        return count

