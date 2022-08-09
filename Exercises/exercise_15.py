manufacturing_price=int(input("Enter the manufacturing price of the product: "))
sellers_percentage=int(input("Enter the seller's percentage: "))
taxes=int(input("Enter the taxes on the manufacturing price: "))
total_price= manufacturing_price + taxes
gain= (sellers_percentage * total_price) / 100

print("The public sale price is" , total_price + gain)
