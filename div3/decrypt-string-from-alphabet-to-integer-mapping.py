class Solution:
    def freqAlphabets(self, s: str) -> str:
         alphabet = 'abcdefghijklmnopqrstuvwxyz'
         result = []
         i = len(s) - 1
        
         while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                result.append(alphabet[num - 1])
                i -= 3
            else:
                result.append(alphabet[int(s[i]) - 1])
                i -= 1
                
         return ''.join(result[::-1])
