class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Notes:
        * use memoization to avoid repeated evaluations by using knowledge of previous evaluated elements
        """
        comp = dict({})
        for i, num in enumerate(nums):
            if comp.get(target - num) != None:
                return [comp.get(target - num), i]
            comp[num] = i