inventory = {
    "books":100,
    "games":132,
    "movies":3
}
def new_inventory():
 if modify == "yes":
     added_item = input("What are you adding to inventory?: ")
     added_quant = int(input(f"How many {added_item} are you adding?: "))
     inventory[added_item] = added_quant
     print("This is what's in stock:")
     for key,value in inventory.items():
         print("{}: {}".format(key,value))
 else:
     print("This is what's in stock then:\n",inventory)

def modify_stock():
    pass
def request_check():
    if initial == "modify":
      #needs to do something with modify variable

initial = input("Would you like to view or modify inventory?: ")
request_check()

modify = input("Would you like to add new inventory? (yes/no) ").lower()
new_inventory()

#need to add other functions like removing inventory, excpetion handling etc..



