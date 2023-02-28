# Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement

# # Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) # -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) # -> "Buddy is sleeping for 10 minutes. His energy is now 15"



class Animal:
   
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        
        

    def play(self, minutes):
        self.energy -= minutes
        print (f"{self.name} is playing for the next {minutes} minutes. When {self.name} is done playing his energy will be at {self.energy}")

    def sleep(self, minutes):
        self.energy +=  minutes
        print(f"{self.name} is sleeping for {minutes} minutes. His energy will be at {self.energy} when he awakes!")

    def eat(self, minutes):
        self.energy *=  minutes
        print(f"{self.name} is eating for {minutes} minutes. His energy will be {self.energy} when it is eaten")


name  = Animal('Buddy', 10)
name2 = Animal('Leo', 10)
name3 = Animal('Frank', 10)


name.play(10)
name.sleep(30)
name2.play(15)