class Solution(object):
    def containsDuplicate(self, nums):
        s1 = set(nums)
        return len(s1) != len(nums)
