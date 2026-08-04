class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen={}
        for num in arr:
            seen[num]=seen.get(num,0)+1
        return len(seen.values())==len(set(seen.values()))
        