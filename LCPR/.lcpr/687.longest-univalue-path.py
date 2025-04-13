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



# @lc code=end
from typing import Optional

# 解法1 
class Solution1:
    # 请在此处实现具体逻辑
    def longestUnivaluePath(self, 参数输入) -> int:
        pass

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
    # def 原始解法header(self, 原始参数) -> int:
    #     return self.solver.原始解法header()



#
# @lcpr case=start
# [5,4,5,1,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,5,4,4,5]\n
# @lcpr case=end

#

