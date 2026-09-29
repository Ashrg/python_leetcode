# 104. 二叉树的最大深度
# 难度：简单
# 标签：树、二叉树、深度优先搜索、广度优先搜索
#
# 给定一个二叉树的根节点 `root`，返回它的最大深度。
#
# 二叉树的**最大深度**是指从根节点到最远叶子节点的最长路径上的节点数。
#
# ### 示例
#
# - 输入：`root = [3,9,20,null,null,15,7]`，输出：`3`
# - 输入：`root = [1,null,2]`，输出：`2`
# - 输入：`root = []`，输出：`0`
#
# ### 提示
#
# - 树中节点的数量在 `[0, 10^4]` 范围内
# - `-100 <= Node.val <= 100`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（节点个数）；第二行为 `n` 个标记（空格分隔），每个标记是整数或 `null`，按层序给出整棵树（`n = 0` 时该行为空行）
# - 输出：一个整数，即最大深度
#
# ACM 输入示例：
# ```
# 7
# 3 9 20 null null 15 7
# ```
# 输出：`3`

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # root 为二叉树根节点（TreeNode），返回最大深度（整数）
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    return max(maxDepth(root.left),maxDepth(root.right))+1
    pass
