#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode.cn/problems/number-of-islands/description/
#
# algorithms
# Medium (62.53%)
# Likes:    2752
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#
from typing import Optional
from  collections import List,deque
# @lc code=start
#* DFS
class Solution_DFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 确认岛屿存在与否
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        # 这里不用visited检查：重复访问被直接修改的cell不影响其cell当前数值
        # dfs目的是将每个(r,c)作为起点的搜索中将四周符合题意的cell变成0
        def dfs(r, c) -> None:
            if r<0 or r>=m or c<0 or c>=n or grid[r][c] == '0':
                # 结束此次递归
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)
        count = 0
        # 外层循环TC是 O(m*n),在dfs中每个cell最多处理一次
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count+=1
        return count 
# TC: O(m*n) 外层循环+内部处理
# SC: O(m*n) 虽然我们没有使用额外的数据结构，但是递归调用本身会占用栈空间，每个递归调用需要存储:
# 局部变量，返回地址，参数值 这些占用的空间与递归深度成正比
#* BFS
class Solution_BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(1, 0),(-1,0),(0, -1), (0,1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    grid[i][j] == '0'

                    queue = deque([(i,j)])
                    while queue:
                        r,c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))
        return count
            
# TC: O(m*n)
# SC: O(min(m, n))

#! 总Solution调用位置
class Solution:
    def __init__(self):
        self.solver = Solution_BFS()  
    def __getattr__(self, name):
        return getattr(self.solver, name)

    
        
# @lc code=end

