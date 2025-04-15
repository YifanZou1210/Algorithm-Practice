#
# @lc app=leetcode.cn id=687 lang=python3
# @lcpr version=30204
#
# [687] 最长同值路径
#

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

# 解法1 : Recursion 
class Solution1:
    """
        初步思路
        1. 最长同值路径即针对某treenode最长diameter,无非是多一个同值限制,该部分分离为一个模块dfs
        2. 利用dfs模块方法再递归遍历子树同时更新最大diameter
    """
    def longestUnivaluePath(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 递归修改全局变量
        max_diameter = 0 
        """
        input: node 递归放入treenode
        output: int 即最大深度
        """
        """
        ? 1. 多解求max_diameter of tree可能吗?各自区别？
        ? 2. 
        """
        def dfs(target:TreeNode,node:TreeNode)->int:
            nonlocal max_diameter
            if not node:
                return 0
            if not target.val == node.val:
                return 0
            if not node.left and not node.right and target.val == node.val:
                return 1
            left_depth, right_depth = dfs(target,node.left), dfs(target, node.right)
            max_diameter = max(max_diameter, left_depth+right_depth)
            return 1+max(left_depth,right_depth)
        # 由于全局设定max-diameter，不能使用recursion递归遍历否则会清空全局递归累加值
        # 采用iteration遍历比如stack, queue等
        queue = deque([root])
        while queue:
            node = queue.popleft()
            dfs(node, node) # 此处修改max-diameter并进行更新保持最大值
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return max_diameter
            
# 解法2
class Solution2:
    # 请在此处实现具体逻辑
    def longestUnivaluePath(self, 参数输入) -> int:
        pass

class Solution:
    def __init__(self):
        # 在这里手动设置选择自己需要运行的解法
        self.solver = Solution1()  # 默认选择递归实现；如需切换请修改为 Solution2() 或其它实现

    # 注意在这里将 SolutionPlaceHolder 换成 lc 题函数名称以及对应的参数和返回值设置
    def longestUnivaluePath(self, root:Optional[TreeNode]) -> int:
        return self.solver.longestUnivaluePath(root)

# @lc code=end

#
# @lcpr case=start
# [5,4,5,1,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,5,4,4,5]\n
# @lcpr case=end

# @lcpr case = start
# []\n
# @lcpr case = end

