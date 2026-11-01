print("===============WELCOME TO SOFIA'S CAFE==============")
menu = {'coffee' : 20,'tea':20,'sandwich':50,'burger':50,'pizza':50,'green tea':50
}
print('-------------------MENU---------------')
print("coffee:20\n tea:20\n sandwich:50\n burger:50\n pizza:50\n green tea:50")
grand_total = 0
while(True):
    order_item = input('Enter your item:').lower()
    if order_item in menu:
        print("price:",menu[order_item])
        quantity = int(input("Enter quantity:"))
        item_total = menu[order_item]*quantity
        print(item_total)
        grand_total += item_total
        choice = input("Do you want anythong else?(yes/no)").lower()
        if choice == 'no':
    
            break
    else:
        print("your item is not available")
print("final bill:RS",grand_total)
