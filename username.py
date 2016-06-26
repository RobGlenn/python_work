
#usernames = ['bob','carol','ted', 'admin']
usernames = []

if usernames == [] :
	print('We need to find more users!')
else:
	for username in usernames :
		if username  == 'admin' :
			print('Hello admin, would you like to see a status report?')
		else :
			print('Hello '+ username.title() + ', thanks for logging in.')


usernames = ['bob','carol','ted', 'alice', 'sue']
new_users = ['jim','scott','jenny','sarah','Carol']

for username in usernames :
	for new_user in new_users :
		if username.lower() == new_user.lower() :
			print(new_user.lower() +' is not available')

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers :
	if number == 1 :
		print( str(number) + 'st')
	elif number == 2 :
		print( str(number) + 'nd')
	elif number == 3 :
		print( str(number) + 'rd')	
	else: 
		print( str(number) + 'th')


