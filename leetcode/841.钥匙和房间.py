#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#
from typing import Optional
from collections import List,defaultdict
# @lc code=start
#* DFS解法
class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        dict = defaultdict(list)
        for i in range(n):
            dict[i].extend(rooms[i])
        def dfs(i):
            visited.add(i)
            for j in dict[i]:
                if j not in visited:
                    dfs(j)
        dfs(0)
        return len(visited) == n
# 设房间数n，总钥匙数E
# TC: O(n+E)遍历rooms一次，开销为O(n+E),每个房间dfs操作总数为E
# SC: O(n+E)

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

