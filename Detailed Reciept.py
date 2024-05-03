item_name = input("What is the item name?: ").title()
item_quant = int(input("How many would you like?: "))
item_price = float(input("How much does each cost?: "))
total_cost = item_price*item_quant
actual_cost = round(total_cost,2)

print('') #just to break up the readability to benefit user

print("Item:",item_name,'\n'+"Quantity:",item_quant,'\n'+"Price per item:",
      item_price,'\n'+"Total cost:",actual_cost)
