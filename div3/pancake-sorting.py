class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        def flip(k):
            arr[:k] = arr[:k][::-1]
            flips.append(k)
        
        n = len(arr)
        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx != target - 1:
                flip(idx + 1)
                flip(target)
        
        return flips
