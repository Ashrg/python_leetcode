# 3. 无重复字符的最长子串
# 难度：中等
# 标签：哈希表、字符串、滑动窗口
#
# 给定一个字符串 `s`，请你找出其中不含有重复字符的**最长子串**（子串要求连续，与子序列不同）的长度。
#
# ### 示例
#
# - 输入：`s = "abcabcbb"`，输出：`3`（最长无重复子串是 `"abc"`）
# - 输入：`s = "bbbbb"`，输出：`1`（最长无重复子串是 `"b"`）
# - 输入：`s = "pwwkew"`，输出：`3`（最长无重复子串是 `"wke"`；注意 `"pwke"` 是子序列，不是子串）
# - 输入：`s = ""`，输出：`0`
#
# ### 提示
#
# - `0 <= s.length <= 5 * 10^4`
# - `s` 由英文字母、数字组成（不含空格）
# - 空串是合法输入，答案为 `0`
#
# ### ACM 模式输入输出格式
#
# - 输入：仅一行，即字符串 `s`（只含字母和数字、不含空格；空串时该行为空行）
# - 输出：一个整数，即最长无重复子串的长度
#
# ACM 输入示例：
# ```
# abcabcbb
# ```
# 输出：`3`

def lengthOfLongestSubstring(s):
    # 返回最长无重复字符子串的长度
    sub = set()

    left = 0
    max_len = 0
    
    for right in range(len(s)):
        #if s[right] not in sub:                #错误2
        #    sub.add(s[right])
        #    max_len += 1
        #else:
        while s[right] in sub:
            sub.remove(s[left])
            left += 1
        sub.add(s[right])                   #错误1 
        max_len = max(max_len, right - left + 1)
    return max_len
    pass
