class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1
        while idx2 > idx1:
            addition = numbers[idx1] + numbers[idx2]  
            if addition == target:
                return [idx1 + 1, idx2 + 1]
            elif addition > target:
                idx2 -= 1
            else:
                idx1 += 1