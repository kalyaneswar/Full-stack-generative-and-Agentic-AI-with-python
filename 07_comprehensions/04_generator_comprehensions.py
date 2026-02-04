daily_sales = [5, 10, 24, 23, 43, 2, 9]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)