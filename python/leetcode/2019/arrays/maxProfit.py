def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return

    min_p = prices[0]
    max_p = 0
    for i in range(1, len(prices)):
        if min_p > prices[i - 1]:
            min_p = prices[i - 1]
        c_p = prices[i] - min_p
        if max_p < c_p:
            max_p = c_p
    return max_p


if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))
    print(maxProfit([]))
    print(maxProfit([1,5]))