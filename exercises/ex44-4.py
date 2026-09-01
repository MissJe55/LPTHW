#Ex 44 - 4 : From Dictionaries to Objects - Creating a Person Constructor

#What happens when you want to create 100 people? You'd have to manually create
#eveny dictionary and add the talk() to each one. Let's create a constructor instead

def Person_new(name, age, eyes):
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
    }

    def talk(words):
        print(f"I am {person['name']} and {words}")

    person['speak'] = talk

    return person

becky = Person_new("Becky", 39, "green")

becky['speak']("I am talking here!")

Jess = Person_new("Jess", 25, "brown")

Jess['speak']("I am talking too!")