class Solution:
    def pivotInteger(self, n: int) -> int:
        total=sum(range(1,n+1))
        left=0
        for ch in range(n+1):
            left+=ch
            if left==total-left+ch:
                return ch
        return -1