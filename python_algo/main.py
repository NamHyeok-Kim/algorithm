def solution(price, money, count):
    price_sum = 0
    for i in range(count):
        price_sum += (i + 1) * price

    answer = price_sum - money

    return max(0, answer)