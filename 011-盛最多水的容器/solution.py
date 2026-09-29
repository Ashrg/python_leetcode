# 11. 盛最多水的容器
# 难度：中等
# 标签：数组、双指针
#
# 给定一个长度为 `n` 的整数数组 `height`。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])`。
#
# 找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。容器的水量由**较短的线的高度 × 两线之间的距离**决定。
#
# ### 示例
#
# - 输入：`height = [1,8,6,2,5,4,8,3,7]`，输出：`49`（选下标 1 和 8 的两条线，`min(8,7) * (8-1) = 49`）
# - 输入：`height = [1,1]`，输出：`1`
# - 输入：`height = [4,3,2,1,4]`，输出：`16`（选两端的线，`min(4,4) * 4 = 16`）
#
# ### 提示
#
# - `n == height.length`
# - `2 <= n <= 10^5`
# - `0 <= height[i] <= 10^4`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（数组长度）；第二行为 `n` 个整数（空格分隔）
# - 输出：一个整数，即最大水量
#
# ACM 输入示例：
# ```
# 9
# 1 8 6 2 5 4 8 3 7
# ```
# 输出：`49`

def maxArea(height):
    # 返回最大水量
    left = 0
    right = len(height) - 1
    max_ = 0
    while left < right:
        h = min(height[left], height[right])
        distance = right - left
        max_ = max(max_, h * distance)
        if h == height[left]:
            left += 1
        else:
            right -= 1
    return max_
    pass
