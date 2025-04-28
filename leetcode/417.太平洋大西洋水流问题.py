#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
from typing import Optional
from collections import List
# @lc code=start
#* DFS解法
class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0),(-1,0),(0,-1),(0,1)]
        pacific, atlantic = [[False]*n for _ in range(m)], [[False]*n for _ in range(m)]
        def dfs(r,c,preh, ocean):
            if r<0 or r>=m or c<0 or c>=n or ocean[r][c] or heights[r][c] < preh:
                return
            ocean[r][c] = True
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr, nc, heights[r][c], ocean)
        for i in range(m):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, n-1, heights[i][n-1], atlantic)
        for j in range(n):
            dfs(0, j, heights[0][j], pacific)
            dfs(m-1, j, heights[m-1][j], atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == atlantic[i][j] == True:
                    res.append([i,j])
        return res
# TC: 
# SC: 
#* xx解法
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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

