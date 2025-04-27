#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
from typing import Optional
from collections import List, defaultdict
# @lc code=start
#! 该题是DAG无环有向图的拓扑排序问题
#! 拓扑排序问题：在 DAG 上找到一个线性序列，使得对任意边 u→v，u 都在 v 之前。常见解法如下：
# 1. DFS后序+反转：对每个节点做 DFS，遍历完所有后继后再把它 append 到结果；最后把结果反转
# 2. Kahn 算法（BFS）：计算每个节点的入度（indegree），把所有入度为 0 的节点入队；依次出队并“移除”它的出边，动态更新入度，产生序列。
#* DFS解法：后序加入+反向DFS
class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        visited = [0]*numCourses
        res = []
        def dfs(u):
            if visited[u] == 1:
                return False
            if visited[u] == 2:
                return True
            visited[u] = 1
            for nei in graph[u]:
                if not dfs(nei):
                    return False
            visited[u] = 2
            res.append(u)
            #? 为什么res不能在递归之前append而要在后序append？
            # 1. DFS前序：一旦进入节点 u 就把它 append(res)，此时它的所有后继 v 并未遍历，无法保证它们后来会出现在 u 之后。
            # 2. DFS后序：等所有后续的依赖（所有 v）都遍历完、都已加入 res 后，才把 u 加入，这就保证了“子节点（依赖）先入栈，父节点后入栈”。
            return True
        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i):
                return []
        return res[::-1]
# TC: O(N+E),N=课程数,E=先修关系数,DFS遍历每条边+每个节点
# SC: O(N+E),存边，递归栈最深N，结果列表也存N个节点
#* xx解法
class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

