favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +
	".")

person = {
	'firstname':'Jules',
	'lastname':'Verne',
	'city':'New York',
}

print(person)	

rivers = {
	'nile':'egypt',
	'mississippi':'USA',
	'amazon':'brazile',
}

for key in rivers.keys() :
	print(key.title())
for value in rivers.values() :
	print(value.title())	
