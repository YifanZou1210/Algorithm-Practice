#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class SolutionRecursion:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        return [] 
    
class SolutionIteration:
    def longestUnivaluePath(self, root:Optional[TreeNode])->int:
        return []

def main():
    nums = [2,7,8,9]
    target = 10
    print(SolutionIteration.longestUnivaluePath(nums,target))
    print(SolutionRecursion.longestUnivaluePath(nums,target))
        
# @lc code=end

