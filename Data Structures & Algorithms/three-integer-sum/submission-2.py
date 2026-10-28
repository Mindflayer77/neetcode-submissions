class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = []
        for ptr3 in range(len(nums)):
            ptr1 = ptr3 + 1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                two_sum = sorted_nums[ptr1] + sorted_nums[ptr2]
                if - sorted_nums[ptr3] == two_sum:
                    triplet = [
                        sorted_nums[ptr1],
                        sorted_nums[ptr2],
                        sorted_nums[ptr3]
                    ]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    ptr1 += 1
                    ptr2 -= 1
                elif two_sum > - sorted_nums[ptr3]:
                    ptr2 -= 1
                else:
                    ptr1 += 1
        return triplets
