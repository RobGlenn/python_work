current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

topping = ""
print('Type q to exit')
while topping != 'q':       
    topping = ""
    topping = input('Topping You want me to add :')
    if topping != 'quit':
      print('I will add ' + topping + ' to your pizza')
print('Thanks for your Order!')

age = ''
total = 0
print('Type q to exit')
while age != 'q':
    age = input('Your age? :')    
    if age =='q':
        break # exit loop
    elif int(age) <= 3:
        print('You get in free')
        print('Total is $' + str(total) + '.00')
    elif int(age) <= 12:
        print('Your ticket is $10.00')
        total = total + 10
        print('Total is $' + str(total) + '.00')
    else:
        print('Your ticket is $15.00')
        total = total + 15
        print('Total is $' + str(total) + '.00')

print('Total is $' + str(total) + '.00')