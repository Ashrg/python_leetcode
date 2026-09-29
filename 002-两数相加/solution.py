# 2. 两数相加
# 难度：中等
# 标签：链表、数学
#
# 给你两个**非空**的链表，表示两个非负的整数。它们每位数字都是按照**逆序**的方式存储的（链表的表头存的是数字的个位），并且每个节点只能存储**一位**数字。
#
# 例如链表 `[2,4,3]` 表示数字 `342`（个位 2、十位 4、百位 3）。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 `0` 之外，这两个数都不会以 `0` 开头。
#
# ### 示例
#
# - 输入：`l1 = [2,4,3], l2 = [5,6,4]`，输出：`[7,0,8]`（因为 342 + 465 = 807）
# - 输入：`l1 = [0], l2 = [0]`，输出：`[0]`
# - 输入：`l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`，输出：`[8,9,9,9,0,0,0,1]`（9999999 + 9999 = 10009998）
#
# ### 提示
#
# - 每个链表中的节点数在范围 `[1, 100]` 内
# - `0 <= Node.val <= 9`
# - 题目数据保证列表表示的数字不含前导零
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（第一条链表长度）；第二行为 `n` 个整数（空格分隔）；第三行为整数 `m`（第二条链表长度）；第四行为 `m` 个整数（空格分隔）
# - 输出：相加结果链表各节点的值（空格分隔）
#
# ACM 输入示例：
# ```
# 3
# 2 4 3
# 3
# 5 6 4
# ```
# 输出：`7 0 8`

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # l1、l2 为两条链表的头节点（ListNode），返回和链表的头节点
    # 注意：请自己定义节点类来创建新节点（判题环境中 ListNode 不可直接引用）
    ans = ListNode()
    t = ans
    carry = 0
    while l1 is not None or l2 is not None:
        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        val = x + y +carry
        t.next = ListNode(val%10)
        carry = val//10
        t = t.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    
    if carry > 0:
        t.next = ListNode(carry)
        t = t.next
    return ans.next
    pass
