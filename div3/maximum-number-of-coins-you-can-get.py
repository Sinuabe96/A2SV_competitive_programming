class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()  
        n = len(piles) // 3  
        total_coins = 0
        for i in range(n, len(piles), 2):
            total_coins += piles[i]
        
        return total_coins
