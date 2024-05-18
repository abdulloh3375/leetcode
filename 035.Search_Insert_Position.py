
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            a = nums.index(target)
            return a
        
        elif target not in nums:
            nums.append(target)
            nums.sort()
            b = nums.index(target)
            return b