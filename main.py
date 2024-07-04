menu = {
    "tea" : 20,
    "milk": 25,
    "coffee" : 27,
    "pizza":30,
    "pasta":25,
    "burger":25,
    "salad":22,
}
total = 0 
print('welcome in our coffee shop')
for x,y in menu.items():
    print(f'{x}:{y}')
order = input('Enter your order: ').lower() 
if order in menu:
    total += menu[order]
    print(f"{order} in progress")
else:
    print('this item invalid')
offer=input('do want to order something else(yes/no): ')
if offer == 'yes':
    order2 = input('what would you add to your order: ') 
    if order2 in menu:
        total += menu[order2]
        print(f'Also {order2} in progress and {order}')
else:
    print('Ok,Have a good time')
print(f'your order cost you: {total}$')