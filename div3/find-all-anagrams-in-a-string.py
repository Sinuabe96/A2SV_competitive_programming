class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        countp = Counter(p)
        count = Counter(s[:len(p)])
        l = 0
        r = len(p)
        while r < len(s):
            if countp == count:
                ans.append(l)
            count[s[l]] -= 1
            if count[s[l]] == 0:
                count.pop(s[l])
            count[s[r]] += 1
            l += 1
            r += 1
            if countp == count:
                ans.append(l)
            return ans
