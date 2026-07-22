class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool(
        """
        maxx=0
        for i,jump in enumerate(nums):
            if i>maxx:
                return False
            maxx=max(maxx,i+jump)
        if maxx>=len(nums)-1:
            return True
        