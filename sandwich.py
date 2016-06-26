# sanwiches

sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

for sandwich in sandwich_orders:
    if sandwich == 'pastrami':
        print('We dont have pastrami today.')
    else:
        print("I made your " + sandwich + " sandwich")
        finished_sandwiches.append(sandwich)

print(finished_sandwiches)
