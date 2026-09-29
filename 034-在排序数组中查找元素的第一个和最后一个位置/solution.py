# 34. 在排序数组中查找元素的第一个和最后一个位置
# 难度：中等
# 标签：数组、二分查找
#
# 给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 `target`，返回 `[-1, -1]`。
#
# 要求算法的时间复杂度为 O(log n)。
#
# ### 示例
#
# - 输入：`nums = [5,7,7,8,8,10], target = 8`，输出：`[3,4]`
# - 输入：`nums = [5,7,7,8,8,10], target = 6`，输出：`[-1,-1]`
# - 输入：`nums = [], target = 0`，输出：`[-1,-1]`
#
# ### 提示
#
# - `0 <= nums.length <= 10^5`
# - `-10^9 <= nums[i] <= 10^9`
# - `nums` 是一个非递减数组
# - `-10^9 <= target <= 10^9`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（数组长度）；第二行为 `n` 个整数（空格分隔；`n = 0` 时该行为空行）；第三行为 `target`
# - 输出：两个整数（空格分隔），即开始位置和结束位置；不存在时输出 `-1 -1`
#
# ACM 输入示例：
# ```
# 6
# 5 7 7 8 8 10
# 8
# ```
# 输出：`3 4`

def searchRange(nums, target):
    # 返回 [开始位置, 结束位置]，不存在返回 [-1, -1]

    left = 0
    right = len(nums) 
    #左边界 找到nums[left] >= target的位置 
    while left < right:
        mid = (left +right)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    if left == len(nums) or nums[left] != target:
        return [-1,-1]
    #找右边界 反向
    lo , hi = left, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return [left,lo - 1]
    pass
