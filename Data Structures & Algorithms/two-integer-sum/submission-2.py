class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [[i, j] for i, n1 in enumerate(nums) for j, n2 in enumerate(nums[i+1:], start=i+1) if n1 + n2 == target][0]