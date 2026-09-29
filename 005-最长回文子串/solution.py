# 5. 最长回文子串
# 难度：中等
# 标签：双指针、字符串、动态规划
#
# 给你一个字符串 `s`，找到 `s` 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
# ### 示例
#
# - 输入：`s = "babad"`，输出：`"bab"`（`"aba"` 同样是有效答案）
# - 输入：`s = "cbbd"`，输出：`"bb"`
# - 输入：`s = "a"`，输出：`"a"`
# - 输入：`s = "ac"`，输出：`"a"`（`"c"` 同样是有效答案）
#
# ### 提示
#
# - `1 <= s.length <= 1000`（本题判题数据额外包含空串用例）
# - `s` 仅由数字和英文字母组成
#
# ### ACM 模式输入输出格式
#
# - 输入：仅一行，即字符串 `s`（为空串时该行是空行）
# - 输出：一个最长回文子串（空串时输出一个空行）
#
# 判题约定：最长回文子串可能有多个，核心代码模式返回其中任意一个都算通过；ACM 模式的测试数据保证最长回文子串唯一，直接输出该子串即可。
#
# ACM 输入示例：
# ```
# cbbd
# ```
# 输出：`bb`

def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    max_len = 1
    begin = 0

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]

            if dp[i][j] and (j - i + 1) > max_len:
                max_len = j - i + 1
                begin = i

    return s[begin : begin + max_len]
    pass
