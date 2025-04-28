#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
from types import Optional
from collections import List, defaultdict
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#* 遍历二叉树收集frequence解法
class Solution1:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dict = defaultdict(int)
        def dfs(node):
            if not node:
                return
            dict[node.val]+=1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        print(dict)
        dfs(root)
        return [key for key, value in dict.items() if value == max(dict.values())]
# TC: O(n)
# SC: O(n)
#* xx解法
class Solution2:
    def 原始function(self, 参数输入) -> int:
        pass
# TC: 
# SC: 

#! 总Solution调用位置
class Solution:
    def __init__(self):
        self.solver = Solution1()  
    def __getattr__(self, name):
        return getattr(self.solver, name)


# @lc code=end

