#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

from collections import deque
from typing import List
from typing import Optional

# @lc code=start
# !解法1: DFS - 如果数据量小，采用DFS是合理的
class SolutionDFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 如果(sr,sc)和color相同，则周围无需要更改的cell
        if image[sr][sc] == color:
            return image
        m, n = len(image), len(image[0])
        old = image[sr][sc]
        # 否则开始修改 
        # 注意不需要visited来记录duplication, 因为修改是一次性行为，后续重复访问无效
        def dfs(r, c):
            # endpoint： 1. 有效的dfs cell 2. 在当前递归中更新此时的color
            if r<0 or r>=m or c<0 or c>=n or image[r][c]!= old:
                return # 停止本次递归检查
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr, sc)
        return image
               
# ! 解法2: BFS - 如果担心stack overflow的话可以采用BFS从当前pixel向外扩展邻居
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        old_color = image[sr][sc]
        if old_color == color:
            return image
        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color # 起点开始染色
        directions = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                #检查边界和颜色
                if 0<=nr<m and 0<=nc<n and image[nr][nc] == old_color:
                    image[nr][nc] = color # 染色
                    queue.append((nr,nc)) # 继续向四周拓展
        return image 

class Solution:
    def __init__(self):
        # 在这里手动设置选择自己需要运行的解法即可，比如 self.solver = Solution xxx
        self.solver = Solution2() 
    def __getattr__(self, name):
        return getattr(self.solver, name)
        
# @lc code=end

