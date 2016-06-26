
#poll dictionary
responses = {}
poll_flag = 'y'

while poll_flag == 'y':
    name = input('What is your name? :')
    responses[name] = name
    response = input('Where would you like to go? :')
    responses[response] = response 
    poll_flag = input('Would you like to add another destination? y/n: ') 

    if poll_flag != 'y':
        continue

print('Finished Poll')

# for name, response in responses.items():
# 	print(name + " would like to go " + response + ".")

for name in responses:
	print(name + " would like to climb " + response + ".")
