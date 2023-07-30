"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        first_dict = {}
        for num in nums1:
            first_dict.setdefault(num, 0)
            first_dict[num] += 1

        second_dict = {}
        for num in nums2:
            second_dict.setdefault(num, 0)
            second_dict[num] += 1

        smaller, bigger = [
            (first_dict, second_dict) if len(first_dict) < len(second_dict) else (second_dict, first_dict)
        ][0]
        for num, count in smaller.items():
            if num in bigger:
                for i in range(min(count, bigger[num])):
                    output.append(num)

        return output
