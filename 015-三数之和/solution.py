# 15. 三数之和
# 难度：中等
# 标签：数组、双指针、排序
#
# 给你一个整数数组 `nums`，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k`，同时还满足 `nums[i] + nums[j] + nums[k] == 0`。请你返回所有和为 `0` 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# ### 示例
#
# - 输入：`nums = [-1,0,1,2,-1,-4]`，输出：`[[-1,-1,2],[-1,0,1]]`
# - 输入：`nums = [0,1,1]`，输出：`[]`
# - 输入：`nums = [0,0,0]`，输出：`[[0,0,0]]`
#
# ### 提示
#
# - `3 <= nums.length <= 3000`
# - `-10^5 <= nums[i] <= 10^5`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（数组长度）；第二行为 `n` 个整数（空格分隔）
# - 输出：每个三元组占一行，组内三个数升序、空格分隔；所有行按三元组字典序升序排列（先比第一个数，相同再比第二个、第三个）；无解时不输出任何内容
#
# ACM 输入示例：
# ```
# 6
# -1 0 1 2 -1 -4
# ```
# 输出：
# ```
# -1 -1 2
# -1 0 1
# ```

def threeSum(nums):
    # 返回所有和为 0 的不重复三元组（每个三元组内部升序）
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n - 2):
       # if nums[i] == nums[i+ 1]: 错误忽略了类似-1 -1 2的答案
       #     continue
        if i > 0 and nums[i] == nums[i - 1]: #换一种去重方式即可 确定-1后进行运算 但是后面i对应值为-1时跳过整个循环
            continue
        if nums[i] > 0: #减少运算 最后全是正数就不用管了
            break
        left = i + 1
        right = n - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                ans.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
    return ans 
    pass
