class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        known = set()
        for num in nums:
            if num in known:
                return True
            known.add(num)
        return False