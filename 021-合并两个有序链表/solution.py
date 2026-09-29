# 21. 合并两个有序链表
# 难度：简单
# 标签：链表、递归
#
# 将两个升序链表合并为一个新的**升序**链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# ### 示例
#
# - 输入：`list1 = [1,2,4], list2 = [1,3,4]`，输出：`[1,1,2,3,4,4]`
# - 输入：`list1 = [], list2 = []`，输出：`[]`
# - 输入：`list1 = [], list2 = [0]`，输出：`[0]`
#
# ### 提示
#
# - 两个链表的节点数目范围是 `[0, 50]`
# - `-100 <= Node.val <= 100`
# - `list1` 和 `list2` 均按**非递减顺序**排列
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（第一个链表长度）；第二行为 `n` 个整数（空格分隔；`n = 0` 时该行为空行）；第三行为整数 `m`（第二个链表长度）；第四行为 `m` 个整数（空格分隔；`m = 0` 时该行为空行）
# - 输出：合并后链表各节点的值（空格分隔；空链表输出一个空行）
#
# ACM 输入示例：
# ```
# 3
# 1 2 4
# 3
# 1 3 4
# ```
# 输出：`1 1 2 3 4 4`

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # list1 / list2 为两条升序链表的头节点（ListNode），返回合并后的头节点
    
    if list1 == None:
        return list2
    if list2 == None:
        return list1

    answer = ListNode()
    if list1.val < list2.val:
        answer.val = list1.val
        list1 = list1.next
    else:
        answer.val =list2.val
        list2 = list2.next
    tmp = answer
    while list1 and list2:
        if list1.val < list2.val:
            new = ListNode()
            new.val = list1.val
            new.next = None
            tmp.next = new
            tmp = tmp.next
            list1 = list1.next
        else:
            new = ListNode()
            new.val = list2.val
            new.next = None
            tmp.next = new
            tmp = tmp.next
            list2 = list2.next
    if list1 == None:
        tmp.next = list2
    else:
        tmp.next = list1
    return answer    
    pass

#修改 原地指针拼接 内存O(1) 
def mergeTwoLists(list1, list2):
    if list1 is None: return list2
    if list2 is None: return list1

    # 1. 确定谁当头节点（不需要 new 任何节点，直接用原有的节点）
    if list1.val < list2.val:
        answer = list1
        list1 = list1.next
    else:
        answer = list2
        list2 = list2.next
        
    tmp = answer
    
    # 2. 循环中直接改变原节点的 .next 指向，而不是 new 新节点
    while list1 and list2:
        if list1.val < list2.val:
            tmp.next = list1  # 直接把现成的 list1 节点接上来
            list1 = list1.next
        else:
            tmp.next = list2  # 直接把现成的 list2 节点接上来
            list2 = list2.next
        tmp = tmp.next        # 尾指针后移
        
    # 3. 拼接剩余部分
    if list1 is None:
        tmp.next = list2
    else:
        tmp.next = list1
        
    return answer

#标准答案:递归  代码更简略
def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2  # 边界：一条为空，直接返回另一条
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)  # list1 头更小，接上剩余部分的合并结果
        return list1
    list2.next = mergeTwoLists(list1, list2.next)
    return list2

#链表的题目另一常见方法为建立哑节点 
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1  
            list1 = list1.next 
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next       
    tail.next = list1 if list1 else list2

    return dummy.next