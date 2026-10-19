#Ex44 - Study Drills 

import random

def Person_new(name, job):
    person = {
        "name": name,
        "job": job,
        "hp" : jobhp[job],

    }
    return person
        
jobhp = {
          "GroundPounder": 600,
          "AmazonWarrior": 350,
          "WebbedSlinger": 225,
     }

damagepower = {
    "GroundPounder" : 51,
    "AmazonWarrior": 39,
    "WebbedSlinger": 25,
}

talkingsmack = {
    "GroundPounder": "Now you and the Earth will shake!",
    "AmazonWarrior": "For Themyscira!",
    "WebbedSlinger": "Time to Hang you out to dry!",

}
    
def whackthem(person1, person2):
    print(f"{person1['name']} throws a huge boulder at {person2['name']}")
    print(f"{talkingsmack[person1['job']]}")
    
    damage = random.randint(1,damagepower[person1['job']])
    person2['hp'] = person2['hp'] - damage


Bruce = Person_new("Incredible Hulk", "GroundPounder")

Diana = Person_new("Wonder Woman", "AmazonWarrior")

Peter = Person_new("Spider Man", "WebbedSlinger")

while Bruce['hp'] >=10 and Diana['hp'] >=10:      
    whackthem(Bruce, Diana) 
    whackthem(Diana, Bruce)

print(f"{Diana['name']} has {Diana['hp']} hit points remaining")
print(f"{Bruce['name']} has {Bruce['hp']} hit points remaining")
print("Fight is over, a new champion reigns!")
