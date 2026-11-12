#Ex 50.2 - A test that imports Person from Ex 50 and confirms it works 

from ex50 import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000, 1000)


    #these asserts are bad,fix them
    assert boxer.hp == 100, "Boxer has the wrong HP"
    assert zombie.hp == 1000, "Zombie has wrong HP"

    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should be alive"

    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead"

    