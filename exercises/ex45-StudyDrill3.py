#Ex 45 - Basic Object Oriented Programming Study Drills

import random

jobhp = {
 "GroundPounder": 1200,
 "AmazonWarrior": 500, 
 "Kryptonite": 1200,
 
 }

damagepower = {
    "GroundPounder" : 225,
    "AmazonWarrior": 110,
    "Kryptonite": 125,
}

talkingsmack = {
    "GroundPounder": "Now you and the Earth will shake!",
    "AmazonWarrior": "For Themyscira!",
    "Kryptonite": "Fear the S on my Chest!",

}
    
class Superhero:

        def __init__(self, name, job): #A class can only have one init
                self.name = name #Three Attributes Stored on the Object
                self.job = job
                self.hp = jobhp[self.job]

                
        def attack(self, target):
                print(f"{self.name} throws a huge boulder at {target.name}")
                print(talkingsmack[self.job])
                damage = random.randint(1, damagepower[self.job])
                target.hp = target.hp - damage
                

                
WonderWoman = Superhero("Diana", "AmazonWarrior")

IncredibleHulk = Superhero("Bruce", "GroundPounder")

while WonderWoman.hp >=10 and IncredibleHulk.hp >=10:
      IncredibleHulk.attack(WonderWoman)
      WonderWoman.attack(IncredibleHulk)

print(" Fight is over, a new champion reigns!")
print(f"{WonderWoman.name} has {WonderWoman.hp} hit points remaining")
print(f"{IncredibleHulk.name} has {IncredibleHulk.hp} hit points remaining")





           




