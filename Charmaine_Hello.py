#
# Charmain, 2026/2/25
# Charmaine_Hello.py
# Print Hello
#

price = 250
units_sold = 1200

total_sales= price * units_sold
discount = total_sales *0.05
net_sales = total_sales - discount

print(f"Total Sales : ${total_sales:,}")
print(f"Discount :${discount:,.2f}")
print(f" Net_Sales : ${net_sales:,.2f}")

quarterly_profit = 85_000

if quarterly_profit> 100_000:
    print("Oustanding quarter - bonus approved.")
elif quarterly_profit > 50_0000:
    print( "Good quarter - on target.")
elif quarterly_profit >0:
    print ("Marginal quarter - review costs.")
else:
    print("Loss this quarter - action required.")

customer_age = 35
account_value = 120_000

if customer_age>= 30 and account_value >= 100_000:
    print("Eligible for premium wealth management services.")
else:
    print("Standard account services apply")

purchase_amount = 100

if purchase_amount>= 500:
    print("10% discount")
elif purchase_amount>=200 and purchase_amount< 500:
    print("5% discount")
elif purchase_amount< 200:
     print("no discount")