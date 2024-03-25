class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         char_count = {}
         for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

         for word in words[1:]:
            current_count = {}
            for char in word:
                if char in char_count and char_count[char] > 0:
                    current_count[char] = current_count.get(char, 0) + 1
                    char_count[char] -= 1
            char_count = current_count

         result = []
         for char, count in char_count.items():
            result.extend([char] * count)
        
         return result
