#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import Optional
from collections import List, defaultdict
# @lc code=start

# * 1. 字典解法
class Solution_Hashmap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict(int)
        for i, num in enumerate(nums):
            if target-num in dict.keys():
                return [i, dict[target-num]]
            dict[num] = i
# TC: O(n), 只遍历一次数组，每次操作哈希表是O(1)总共n次操作
# SC: O(n),最坏情况下，字典存下真个个数组中的每个元素和下标
# * 2. 暴力解法
class Solution_Brute_Force:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
# TC: O(n^2) - 外层循环n，内层循环worst condition是n-1,n-2,...总共比较次数是 n(n-1)/2即 O(n^2)
# SC: O(1) - 没有使用额外数据结构仅用了临时变量i, j占用的是常量空间             

#! 总Solution调用位置
class Solution:
    def __init__(self):
        self.solver = Solution_Brute_Force()  
    def __getattr__(self, name):
        return getattr(self.solver, name)

# @lc code=end

