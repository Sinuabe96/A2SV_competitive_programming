class Solution:
    def similarPairs(self, words: List[str]) -> int:
         def areSimilar(word1, word2):
             return set(word1) == set(word2)

         count = 0
         n = len(words)

         for i in range(n):
            for j in range(i + 1, n):
                if areSimilar(words[i], words[j]):
                    count += 1

         return count
