# 136. 只出现一次的数字
# 难度：简单
# 标签：位运算、数组
#
# 给你一个**非空**整数数组 `nums`，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度、且不使用额外空间的算法来解决此问题。
#
# ### 示例
#
# - 输入：`nums = [2,2,1]`，输出：`1`
# - 输入：`nums = [4,1,2,1,2]`，输出：`4`
# - 输入：`nums = [1]`，输出：`1`
#
# ### 提示
#
# - `1 <= nums.length <= 3 * 10^4`
# - `-3 * 10^4 <= nums[i] <= 3 * 10^4`
# - 除了某个元素只出现一次以外，其余每个元素均出现两次
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（数组长度）；第二行为 `n` 个整数（空格分隔）
# - 输出：一个整数，即只出现一次的元素
#
# ACM 输入示例：
# ```
# 5
# 4 1 2 1 2
# ```
# 输出：`4`

def singleNumber(nums):
    # 返回只出现一次的那个整数

    #思路 利用哈希表查找 需要开空间 利用异或操作的特性即可省空间
    compared = set()

    for i in range(len(nums)):
        if nums[i] in compared:
            compared.remove(nums[i])
        else:
            compared.add(nums[i])
    
    return compared.pop()


    #result = 0
    #for i in range(len(nums))
    #   result ^= nums[i]
    #return result
    pass
