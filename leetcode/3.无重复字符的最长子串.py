#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from typing import Optional

#* xx解法
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index: dict[str, int] = {}
        left: int = 0
        max_len: int = 0
        # 右指针（right）从 0 遍历到 len(s)-1，char 为当前字符
        for right, char in enumerate(s):
            # 如果当前字符曾出现且位置在窗口内（last_index[char] >= left）：
            if char in last_index and last_index[char] >= left:
                # 将左指针跳到上次出现位置的下一位，维护窗口内无重复
                # 必须保证 left 单调不减，避免回退导致边界逻辑错误
                left = last_index[char] + 1
            last_index[char] = right
            # 计算当前窗口长度 (right - left + 1)，并更新最大值
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len  
# TC: O(n), n = len(s), right指针遍历一次，left指针最多向右移动n次，哈手表查找/更新都是O(1)
# SC: O(min(m, n))n=len(s),m是字符集大小，哈希表 last_index 最多只会存入不重复字符的键值对，又不可能超过字符集的总量 m；
# 所以说 last_index最多存放m个键值对
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

