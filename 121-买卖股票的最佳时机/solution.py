# 121. 买卖股票的最佳时机
# 难度：简单
# 标签：数组、动态规划
#
# 给定一个数组 `prices`，其中 `prices[i]` 表示某支股票第 `i` 天的价格。
#
# 你只能选择**某一天**买入这只股票，并选择在**未来的某一个不同的日子**卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0`。
#
# ### 示例
#
# - 输入：`prices = [7,1,5,3,6,4]`，输出：`5`（第 2 天买入（价格 1），第 5 天卖出（价格 6），利润为 5）
# - 输入：`prices = [7,6,4,3,1]`，输出：`0`（价格一路下跌，不交易利润为 0）
#
# ### 提示
#
# - `1 <= prices.length <= 10^5`
# - `0 <= prices[i] <= 10^4`
#
# ### ACM 模式输入输出格式
#
# - 输入：第一行为整数 `n`（天数）；第二行为 `n` 个整数（空格分隔，每天的价格）
# - 输出：一个整数，即最大利润
#
# ACM 输入示例：
# ```
# 6
# 7 1 5 3 6 4
# ```
# 输出：`5`

def maxProfit(prices):
    # 返回最大利润（整数）
    minPrice = prices[0]
    best = 0

    for i in range(1, len(prices)):
        if prices[i] - minPrice > best:
            best = prices[i] - minPrice
        if prices[i] < minPrice:
            minPrice = prices[i]
    
    return best    

    pass
