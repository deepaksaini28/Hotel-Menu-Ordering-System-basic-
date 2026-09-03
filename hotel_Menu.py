#difine the menu of restarant
menu = {
    'pizza':100,
    'pasta':90,
    'coffee':80,
    'chai':40,
}

#Greet
print("Welcome Deepak Restarant")
print("Pizza : 100\nPasta : 90\nCoffee : 80\nChai : 40")

order_total = 0
#100 + 90 = 190

item_1 = input("Enter the name of the item you want to order: ").strip().lower()
if item_1 in menu:
    order_total +=menu[item_1] #0 + 100
    print (f"Your item {item_1} has been added to your order")

else:
    print(f"Order item {item_1} is not available yet")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("enter the name of second item =").strip().lower()
    if item_2 in menu:
        order_total += menu[item_2] #190 + 90
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Order item {item_2} is not available yet")

print(f"Your total order amount is : {order_total}")