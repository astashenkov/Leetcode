"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        data_dict = {}
        result = []
        for items in nums:
            if items in data_dict:
                result.append(items)
            else:
                data_dict[items] = 1
        return result
