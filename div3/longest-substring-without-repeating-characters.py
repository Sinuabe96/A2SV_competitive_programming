class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in s:
            for j in s:
                subs = s.substring(i, j+1)
                if uniqueChars(subs):
                    result = max(result, len(subs))
