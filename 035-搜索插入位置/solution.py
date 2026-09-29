# 35. 搜索插入位置
# 难度：简单
# 标签：数组、二分查找
#
# 给定一个升序排列、元素互不相同的整数数组 `nums` 和一个整数目标值 `target`，请你在数组中找出 `target`，并返回其下标。如果目标值不存在于数组中，返回它将会被按顺序插入的位置（下标从 0 开始）。
#
# 要求算法的时间复杂度为 O(log n)。
#
# ### 示例
#
# - 输入：`nums = [1,3,5,6], target = 5`，输出：`2`
# - 输入：`nums = [1,3,5,6], target = 2`，输出：`1`
# - 输入：`nums = [1,3,5,6], target = 7`，输出：`4`
#
# ### 提示
#
# - `1 <= nums.length <= 10^4`
# - `-10^4 <= nums[i] <= 10^4`
# - `nums` 为无重复元素的升序数组
# - `-10^4 <= target <= 10^4`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（数组长度）；第二行为 `n` 个升序整数（空格分隔）；第三行为 `target`
# - 输出：一个整数（目标值下标，或它应按顺序插入的位置）
#
# ACM 输入示例：
# ```
# 4
# 1 3 5 6
# 5
# ```
# 输出：`2`

def searchInsert(nums, target):
    # 返回目标值下标，或它应按顺序插入的位置（整数）
    left = 0
    right = len(nums)-1
    if nums[right] == target:
        return right
    mid = int((left + right)/2)

    if nums[mid] == target:
        return mid
    
    if nums[left] > target:
        return 0
    
    if nums[right] < target:
        return len(nums)

    while nums[mid] != target:
        if nums[mid] > target:
            right = mid - 1
            # if (right - left) == 1:
            #    return right
            if right == left:
                return right + 1
        else:
            left = mid + 1
            if (right - left) == 1:
                return left
            
        
        mid = int((left + right) / 2)
    
    return mid
    pass
