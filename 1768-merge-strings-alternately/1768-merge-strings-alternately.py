class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=[]
        len1,len2=len(word1),len(word2)
        i,j=0,0
        while i<len1 and j<len2:
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
        
        