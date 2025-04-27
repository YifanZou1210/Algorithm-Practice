#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode.cn/problems/course-schedule/description/
#
# algorithms
# Medium (55.22%)
# Likes:    2140
# Dislikes: 0
# Total Accepted:    548K
# Total Submissions: 991.3K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
# ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 
# 
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 
# 
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 
# 示例 2：
# 
# 
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
# 
# 
# 
# 提示：
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同
# 
# 
#
from typing import List, Optional
from collections import defaultdict
# @lc code=start
#* DFS解法
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        #: ------- 构建邻接表,TC = O(E)
        for v, u in prerequisites:
            graph[u].append(v)
        dict = [0]*numCourses
        def dfs(u):
            if dict[u] == 1: return False
            if dict[u] == 2: return True
            dict[u] = 1 # 开始遍历
            #:------ DFS内部操作： 虽然有嵌套循环，但是由于条件限制，边和顶点都只会访问一次,TC=O(1)
            for v in graph[u]:
                # 在递归过程中，只要检测到一个环就能确定无法实现所有的递归
                # 但是要实现所有的遍历才能确定是否无环，所以这里要用not dfs作为negative condition
                if not dfs(v):
                    return False
            dict[u] = 2 # 结束遍历
            return True # 遍历完成
        # 图不一定连通，需要对所有course递归遍历
        for i in range(numCourses):
            #:------ DFS遍历 TC= O(V)
            if dict[i] == 0:
                if not dfs(i):
                    return False
        return True
# TC: O(V+E),V课程数量,E先决条件数量,
# SC: O(V+E),构建邻接表O(E),存储重复表O(V),递归调用栈最深最坏最坏情况是O(V)，即最长递归调用链是V的长度
#* BFS解法
class Solution_BFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

