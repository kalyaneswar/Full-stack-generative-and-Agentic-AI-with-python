tea_prices_inr = {
    "Masala Chai": 30,
    "Green Tea": 45,
    "Lemon Tea": 200
}

tea_prices_usd = {
    tea:price / 80 for tea, price in tea_prices_inr.items() 
}

print(tea_prices_usd)