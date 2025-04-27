#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#
# https://leetcode.cn/problems/employee-importance/description/
#
# algorithms
# Medium (69.33%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    87K
# Total Submissions: 125.4K
# Testcase Example:  '[[1,5,[2,3]],[2,3,[]],[3,3,[]]]\n1'
#
# 你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。
# 
# 给定一个员工数组 employees，其中：
# 
# 
# employees[i].id 是第 i 个员工的 ID。
# employees[i].importance 是第 i 个员工的重要度。
# employees[i].subordinates 是第 i 名员工的直接下属的 ID 列表。
# 
# 
# 给定一个整数 id 表示一个员工的 ID，返回这个员工和他所有下属的重要度的 总和。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# 输出：11
# 解释：
# 员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 =
# 11 。
# 
# 
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：employees = [[1,2,[5]],[5,-3,[]]], id = 5
# 输出：-3
# 解释：员工 5 的重要度为 -3 并且没有直接下属。
# 因此，员工 5 的总重要度为 -3。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= employees.length <= 2000
# 1 <= employees[i].id <= 2000
# 所有的 employees[i].id 互不相同。
# -100 <= employees[i].importance <= 100
# 一名员工最多有一名直接领导，并可能有多名下属。
# employees[i].subordinates 中的 ID 都有效。
# 
# 
#
from types import List
from typing import Optional
# @lc code=start
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
#* DFS解法
class Solution_DFS:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # 1. 构建 id -> Employee 对象的映射（O(n)）
        emp_map = {emp.id: emp for emp in employees}  # emp_map: Dict[int, Employee]
        visited = set()  # 可选，用于防止潜在的循环依赖
        def dfs(eid: int) -> int:
            if eid in visited:
                return 0
            visited.add(eid)
            if eid not in emp_map:
                return 0
            emp = emp_map[eid] 
            total = emp.importance  
            for sub_id in emp.subordinates: 
                total += dfs(sub_id)
            return total
        return dfs(id)

# TC: 
# SC: 
#* xx解法
class Solution2:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
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

