#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# @lc code=start
#* 双指针解法
class Solution_Two_Pointers:
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #? 1. 任意l1,l2 空影响结果？如何处理？最优处理方案减少代码量？
        # 1. A：对于担心是否为空而影响执行的链表题目，可以用哑节点dummy node处理，value随意设置，最终返回的是`dummynode.next`
        #? 2. 处理l1,l2全空容易，但是是否合理有必要？
        # 2. A：该问题回答和上面一样
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
# TC: O(max(m, n))：整个循环中每次处理一个节点, m-l1, n-l2，最多执行max(m,n)+1次，traversal一次最长链表长度，外加一次可能的进位
# SC: O(max(m, n)): 新建链表，长度为max(m, n+1，其他常量变量val1, val2, carry, current, dummy是O(1)的常量空间

#* xx解法
class Solution2:
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass
# TC: 
# SC: 

#! 总Solution调用位置
class Solution:
    def __init__(self):
        self.solver = Solution_Two_Pointers()  
    def __getattr__(self, name):
        return getattr(self.solver, name)
   
        
# @lc code=end

