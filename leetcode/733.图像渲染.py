#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

from typing import List


from typing import Optional

# @lc code=start
# 解法1 
class Solution1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 如果(sr,sc)和color相同，则周围无需要更改的cell
        if image[sr][sc] == color:
            return image
        # 否则开始修改 
        # 注意不需要visited来记录duplication, 因为修改是一次性行为，后续重复访问无效
        def dfs(r, c):
            # endpoint： 1. 有效的dfs cell 2. 更新
            
        
# 解法2
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pass
        

class Solution:
    def __init__(self):
        # 在这里手动设置选择自己需要运行的解法
        self.solver = Solution1()  # 默认选择递归实现；如需切换请修改为 Solution2() 或其它实现

    # 注意在这里将 SolutionPlaceHolder 换成 lc 题函数名称以及对应的参数和返回值设置
    # def 原始解法header(self, 原始参数) -> int:
    #     return self.solver.原始解法header()



    
        
# @lc code=end

