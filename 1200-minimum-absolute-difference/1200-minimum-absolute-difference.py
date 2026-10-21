class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        mini=float('inf')
        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            if diff<mini:
                mini=diff
        result=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==mini:
                result.append([arr[i-1],arr[i]])
        return result

        