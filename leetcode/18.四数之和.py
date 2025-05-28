#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List, Optional

#* Two Pointer 解法
class Solution_2P:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    # 题目4sum要求返回所有不重复且和等于目标值的四元组，若不在枚举过程中跳过相同的nums[i],会多次声称内容相同但索引不同的四元组最终结果会出现重复组合
        nums.sort()
        n = len(nums)
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r = j+1,n-1
                while l<r:
                    t=nums[i]+nums[j]+nums[l]+nums[r]
                    if t==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif t<target:
                        l+=1
                    else:
                        r-=1
        return res

# TC: O(n^2)
# SC: O(n)
# #* xx解法
# class Solution2:
#    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
# TC: 
# SC: 

#! 总Solution调用位置
class Solution:
    def __init__(self):
        self.solver = Solution_2P()  
    def __getattr__(self, name):
        return getattr(self.solver, name)

        
# @lc code=end

