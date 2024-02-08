commission_rate_purchase = float(input("Enter commission rate percentage on stock purchase: "))
commission_rate_sale = float(input("Enter commission rate percentage on stock sale: "))
num_shares_purchased = int(input("Enter number of shares purchased: "))
num_shares_sold = int(input("Enter number of shares sold: "))
purchase_price_per_share = float(input("Enter purchase price per share: "))
sell_price_per_share = float(input("Enter sell price per share: "))


amount_paid = num_shares_purchased * purchase_price_per_share
commission_paid_on_purchase = amount_paid * commission_rate_purchase
amount_the_stock_sold_for = num_shares_sold * sell_price_per_share
commission_paid_on_sale = amount_the_stock_sold_for * commission_rate_sale
profit = amount_the_stock_sold_for - amount_paid - commission_paid_on_purchase - commission_paid_on_sale
net = profit - commission_paid_on_purchase - commission_paid_on_sale


print("Amount paid for the stock: $%.2f" % amount_paid)
print("Commission paid on the purchase: $%.2f" % commission_paid_on_purchase)
print("Amount the stock sold for: $%.2f" % amount_the_stock_sold_for)
print("Commission paid on the sale: $%.2f" % commission_paid_on_sale)
print("Profit (or loss if negative): $%.2f" % profit)
print("")
