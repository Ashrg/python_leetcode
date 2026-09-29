# 101. 对称二叉树
# 难度：简单
# 标签：树、深度优先搜索、广度优先搜索、二叉树
#
# 给你一个二叉树的根节点 `root`，检查它是否轴对称。
#
# 即判断这棵树是否关于根节点左右镜像对称：左子树与右子树互为镜像（对应位置节点值相同，且结构互为镜像）。
#
# ### 示例
#
# - 输入：`root = [1,2,2,3,4,4,3]`，输出：`true`
# - 输入：`root = [1,2,2,null,3,null,3]`，输出：`false`（虽然对应位置的值看起来对称，但两棵子树的结构并不互为镜像）
# - 输入：`root = []`，输出：`true`
#
# （数组为二叉树的层序遍历表示，`null` 表示空节点）
#
# ### 提示
#
# - 树中节点数目在范围 `[0, 1000]` 内
# - `-100 <= Node.val <= 100`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（层序序列长度）；第二行为 `n` 个标记（空格分隔），每个标记为整数或 `null`，按层序描述二叉树（`n = 0` 时该行为空行，表示空树）
# - 输出：`true` 或 `false`（小写）
#
# ACM 输入示例：
# ```
# 7
# 1 2 2 3 4 4 3
# ```
# 输出：`true`

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    # root 为二叉树根节点（TreeNode），返回是否轴对称（布尔值）
    def match_tree(l1,l2):
        if l1 is None and l2 is None:
            return True
        if l1 is None or l2 is None:
            return False

        if l1.val == l2.val and match_tree(l1.left,l2.right) and match_tree(l1.right,l2.left):
            return True
        return False
    if root is None:
        return True
    return match_tree(root.left,root.right)
    pass
