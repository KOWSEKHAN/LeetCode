class Solution(object):
    def twoSum(self, nums, target):
       n_dict={}
       for i,num in enumerate(nums):
        c=target-num
        if c in n_dict:
            return [n_dict[c],i]
        n_dict[num]=i 