def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

order = [50, 100, 150]

for price in order:
    final_amount = add_vat(price , 10)
    print(f"Orginal: {price}, final with VAT: {final_amount}")