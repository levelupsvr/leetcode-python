class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low=prices[0]
        high=0
        for ch in prices:
            if ch<low:
                low=ch
            else:
                target=ch-low
                if target>high:
                    high=target
        return high
        