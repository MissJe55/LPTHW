states = {
    'New York': 'NY',
    'North Carolina': 'NC',
    'Virginia': 'VA',
    'Florida': 'FL',
    'Rhode Island': 'RI'
}

#Create a basic set of states and some cities in them

cities = {
    'NC': 'Raleigh',
    'VA': 'Richmond',
    'FL': 'Jacksonville',
    'RI': 'South Falls'
}

#Add some more cities
cities['NY'] = 'New York'
cities['FL'] = 'Tallahasee'

#Print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("FL State has: ", cities['FL'])

#Print some states
print('-' * 10)
print("Virginia's abbreviation is: ", states['Virginia'])
print("Florida's abbreviation is: ", states['Florida'])

#Do it by using the state then cities dict
print('-' * 10)
print("North Carolina has: ", cities[states['North Carolina']])
print("Florida has ", cities[states['Florida']])

#Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#Print every city in the state
print('-' * 10)
for abbrev, city in list (cities.items()):
    print(f"{abbrev} has the city {city}")

#Now do the same for both
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f" and has city {cities[abbrev]}")

print('-' * 10)
#Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

#Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for state 'TX' is: {city}")