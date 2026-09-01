#Ex 44 -2 : Dictionaries and Objects
# Function now at the top and placed inside the Jessica Dict



def talk(who, words): #moved here to be referenced later
    print(f"I am {who['name']} and {words}")

Jessica = {
    "name": "Jessica",
    "age": 47,
    "talk": talk  #Talk function passed in dict
}

Jessica['talk'](Jessica, "I am talking here!")  


#Exploring function definition before a dictionary, passing the function to the dictionary, 
# and calling it with dictionary in mind