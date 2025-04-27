#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
# https://leetcode.cn/problems/number-of-provinces/description/
#
# algorithms
# Medium (62.55%)
# Likes:    1199
# Dislikes: 0
# Total Accepted:    347.4K
# Total Submissions: 555.3K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 
# 
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c
# 间接相连。
# 
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而
# isConnected[i][j] = 0 表示二者不直接相连。
# 
# 返回矩阵中 省份 的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from collections import List
from typing import Optional
# @lc code=start
#* DFS解法
from typing import List

class Solution_DFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :param isConnected: List[List[int]]  # adjacency matrix (n x n)
        :return: int                         # number of connected components
        """
        n = len(isConnected)                  # 城市总数 / number of cities
        visited = [False] * n                 # visited[i] 表示城市 i 是否已访问

        def dfs(city: int):
            """
            从 city 出发，标记同一连通分量内所有城市
            :param city: int  当前访问的城市编号
            """
            for nei in range(n):              # 遍历 city 的所有可能邻居
                # 如果 city 与 nei 相连且 nei 尚未访问
                if isConnected[city][nei] == 1 and not visited[nei]:
                    visited[nei] = True       # 标记访问
                    dfs(nei)                  # 递归访问 nei 的邻居

        count = 0
        # 对每个城市 i，如果它没被访问，就意味着找到一个新省份
        for i in range(n):
            if not visited[i]:
                visited[i] = True            # 标记 i 已访问
                dfs(i)                        # 启动 DFS，遍历完整个省份
                count += 1                   # 省份数量 +1

        return count
# TC: O(n^2)由于对于每个cell都要进行一次dfs
# SC: O(n)
#* xx解法
class Solution_BFS:
    def 原始function(self, 参数输入) -> int:
        pass
# TC: 
# SC: 
#! 总Solution调用位置
class Solution:
    def __init__(self):
        self.solver = Solution_DFS()  
    def __getattr__(self, name):
        return getattr(self.solver, name)

        
# @lc code=end

