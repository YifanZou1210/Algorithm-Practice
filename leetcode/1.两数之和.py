#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import Optional
from collections import List, defaultdict
# @lc code=start

class Solution_Hashmap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict(int)
        for i, num in enumerate(nums):
            if target-num in dict.keys():
                return [i, dict[target-num]]
            dict[num] = i

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass

class Solution:
    def __init__(self):
        self.solver = Solution_Hashmap()  
    def __getattr__(self, name):
        return getattr(self.solver, name)

# @lc code=end

