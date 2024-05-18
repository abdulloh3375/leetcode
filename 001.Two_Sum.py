
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



        for i, element in enumerate(nums):
            for j, son_2 in enumerate(nums):
                if son_2 + element == target and i != j:
                    return[i,j]
