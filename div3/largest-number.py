class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0] == "0":
            return "0"
        return "".join(nums_str)
