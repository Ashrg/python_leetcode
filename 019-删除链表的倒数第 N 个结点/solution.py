# 19. 删除链表的倒数第 N 个结点
# 难度：中等
# 标签：链表、双指针
#
# 给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。
#
# ### 示例
#
# - 输入：`head = [1,2,3,4,5], n = 2`，输出：`[1,2,3,5]`
# - 输入：`head = [1], n = 1`，输出：`[]`
# - 输入：`head = [1,2], n = 1`，输出：`[1]`
#
# ### 提示
#
# - 链表中结点的数目为 `sz`，`1 <= sz <= 30`
# - `0 <= Node.val <= 100`
# - `1 <= n <= sz`（`n` 等于链表长度时删除的是头结点）
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `len`（链表长度）；第二行为 `len` 个整数（空格分隔）；第三行为 `n`
# - 输出：删除后链表各节点的值（空格分隔；空链表输出一个空行）
#
# ACM 输入示例：
# ```
# 5
# 1 2 3 4 5
# 2
# ```
# 输出：`1 2 3 5`

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # head 为链表头节点（ListNode），返回删除后的头节点
    dummy = ListNode(0, head)  #错因 对链表的理解不足
    #fast = ListNode(0, head)
    #low = ListNode(0, head)
    fast = low = dummy
    for i in range(n):
        fast = fast.next
    
    while fast.next is not None:
        fast = fast.next
        low = low.next
    
    low.next = low.next.next
    return dummy.next
    pass
