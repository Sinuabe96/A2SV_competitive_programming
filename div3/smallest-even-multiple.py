class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        lcm_2_n = (2 * n) // math.gcd(2, n)
        return lcm_2_n


solution = Solution()
print(solution.smallestEvenMultiple(5))  
print(solution.smallestEvenMultiple(6)) 
