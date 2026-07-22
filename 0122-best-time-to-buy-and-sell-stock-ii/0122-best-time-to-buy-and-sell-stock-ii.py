class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxx=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxx+=prices[i]-prices[i-1]
        return maxx


        