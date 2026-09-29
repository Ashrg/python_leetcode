# 94. 二叉树的中序遍历
# 难度：简单
# 标签：树、二叉树、深度优先搜索
#
# 给定一个二叉树的根节点 `root`，返回它的中序遍历结果（左子树 → 根节点 → 右子树）。
#
# ### 示例
#
# - 输入：`root = [1,null,2,3]`，输出：`[1,3,2]`
# - 输入：`root = []`，输出：`[]`
# - 输入：`root = [1]`，输出：`[1]`
#
# ### 提示
#
# - 树中节点数目在范围 `[0, 100]` 内
# - `-100 <= Node.val <= 100`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（层序表示的长度）；第二行为 `n` 个标记（整数或 `null`，按层序给出，`null` 表示空节点；`n = 0` 时该行为空行）
# - 输出：中序遍历结果（空格分隔；空树输出一个空行）
#
# ACM 输入示例：
# ```
# 4
# 1 null 2 3
# ```
# 输出：`1 3 2`

def inorderTraversal(root):
    # root 为二叉树根节点（TreeNode），返回中序遍历结果列表
    ans = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        ans.append(node.val) #
        dfs(node.right)
    
    dfs(root)    
    return ans
    pass
