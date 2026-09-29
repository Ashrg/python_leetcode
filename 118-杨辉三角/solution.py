# 118. 杨辉三角
# 难度：简单
# 标签：数组、数学、动态规划
#
# 给定一个非负整数 `numRows`，生成「杨辉三角」的前 `numRows` 行。
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# ### 示例
#
# - 输入：`numRows = 5`，输出：`[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`
# - 输入：`numRows = 1`，输出：`[[1]]`
#
# ### 提示
#
# - `1 <= numRows <= 30`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `numRows`
# - 输出：共 `numRows` 行，每行输出一层（数字空格分隔）
#
# ACM 输入示例：
# ```
# 5
# ```
# 输出：
# ```
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# ```

def generate(numRows):
    # 返回杨辉三角前 numRows 行（二维列表）
    ans = []
    for i in range(numRows):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
        ans.append(row)
    return ans
    pass
