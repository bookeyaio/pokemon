class Pokemon:
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False 
        
    def __repr__(self):
        #If you print out the name of the pokemon it will display the name type level and the amount of health that pokemon has
        return "{} is a {} type pokemon and is level {}. They have {} points of health".format(self.name,self.type,self.level,self.health)
    
    def lose_health(self,lost_health):
        self.health - lost_health
        print("Your pokemon lost {} points of health".format(lost_health))
        if self.health <= 0:
            self.health = 0
            self.is_knocked_out = True
            return self.knock_out()

    def gain_health(self,health_potion):
        self.health + health_potion
        print("Your pokemon is gaining {} points of health".format(health_potion))
            
    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print("Your pokemon is knocked out!")
        

    def revive_pmon(self):
        if self.health == 0:
            self.health = 5
            print("Your pokemon has been revived!")
   
    def attack(self,other_pmon):
        #Super effective attacks to an opposing pokemon
        if (self.type == "water" and other_pmon.type == "fire") or (self.type == "fire" and other_pmon.type == "grass") or (self.type == "grass" and other_pmon.type == "water"):
            sedamage = other_pmon.level * 2
            other_pmon.lose_health(sedamage)
            print("Super effective! You damaged the opposing pokemon and they have {} points of health left".format(other_pmon.health))
        
        #Not very effective attacks to an opposing pokemon
        if (self.type == "fire" and other_pmon.type == "water") or (self.type == "water" and other_pmon.type == "grass") or (self.type == "water" and other_pmon.type == "grass"):
            nedamage = other_pmon.level / 2
            other_pmon.lose_health(nedamage)
            print("Not very effective! You damaged the opposing pokemon and they have {} points of health left".format(other_pmon.health))
        
        #Pokemon of same type attacks to an opposing pokemon
        if (self.type == other_pmon.type):
            other_pmon.lose_health(other_pmon.level)


class Trainer:
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self):
        #this will represent the name of the trainer along with how many health potions they have 
        print("The trainer {} is going into battle with".format(self.name))
        for poke in self.pokemons:
            print(poke)

    def use_potion(self,num_potions):
        if num_potions > 0:
            print("You have used {} potion to heal {}".format(self.potions,self.pokemons[self.current_pokemon]))
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
            print("{} has gained 20 health".format(self.pokemons[self.current_pokemon]))

    def attack_trainer(self,other_trainer):
        my_pmon = self.pokemons[self.current_pokemon]
        other_trainer_pmon  = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pmon.attack(other_trainer_pmon)
        print("You are attacking the opposing trainers pokeon with {}".format(my_pmon))

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)


a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)
trainer_one = Trainer([a,b,c], 3, "Ashe")
trainer_two =  Trainer([d,e,f], 3 , "Connor")



# Testing attacking, giving potions, and switching pokemon.
trainer_one.attack_trainer(trainer_two)
trainer_two.attack_trainer(trainer_one)
trainer_two.use_potion(1)
trainer_one.attack_trainer(trainer_two)
