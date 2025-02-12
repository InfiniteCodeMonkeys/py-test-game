import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} has {opponent.health} health remaining.")
 
    def is_alive(self):
        return self.health > 0
   
    def __str__(self):
        return f"{self.name}: {self.health} HP, {self.attack_power} AP"
    
class Hero(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.healing_potions = 3  

    def heal(self):
        if self.healing_potions > 0:
            heal_amount = random.randint(10, 30)
            self.health += heal_amount
            self.healing_potions -= 1
            print(f"{self.name} heals for {heal_amount} health! Potions left: {self.healing_potions}")
        else:
            print("No healing potions left!")
    
    def defend(self):
        print(f"\n🛡️ {self.name} prepares to defend, reducing the next attack's damage!")
        return True  # Return True to indicate defense mode
    
class Dragon(Character):
    def __init__(self, name="Dragon", health=120, attack_power=20):
        super().__init__(name, health, attack_power)
        self.fire_breath = 3  # Number of fire breath attacks available

    def fire_attack(self, opponent):
        if self.fire_breath > 0:
            damage = random.randint(15, self.attack_power)
            opponent.health -= damage
            self.fire_breath -= 1
            print(f"{self.name} uses fire breath on {opponent.name} for {damage} damage! Fire breaths left: {self.fire_breath}")
        else:
            print(f"{self.name} has no fire breath attacks left!")

    def choose_attack(self, opponent):
        if self.fire_breath > 0 and random.random() < 0.3:
            self.fire_attack(opponent)
        else:
            super().attack(opponent)


def battle():
    print("\n🐉 Welcome to Dragon Slayer! 🏰")
    hero_name = input("Enter your hero's name: ")
    hero = Hero(hero_name, 100, 15)
    dragon = Dragon()

    while hero.is_alive() and dragon.is_alive():
        print("\n✨ Your Turn!")
        print("1️⃣ Attack")
        print("2️⃣ Defend")
        print("3️⃣ Heal")
        print("4️⃣ Run")

        choice = input("Choose an action: ")

        if choice == "1":
            hero.attack(dragon)
        elif choice == "2":
            hero.defend()
        elif choice == "3":
            hero.heal()
        elif choice == "4":
            print("\n🏃 You run away! Game Over.")
            return
        else:
            print("\n❌ Invalid choice!")
            continue

        if dragon.is_alive():
            print("\n🐉 Dragon's Turn!")
            if choice == "2":  # Reduce damage if defending
                print("🛡️ Your defense absorbs some damage!")
                dragon.choose_attack(hero)
                hero.health += 5  # Reduce damage slightly
            else:
                dragon.choose_attack(hero)

        print(f"\n❤️ {hero.name} HP: {hero.health} | 🐉 Dragon HP: {dragon.health}")

    if hero.is_alive():
        print("\n🎉 You slayed the dragon! Victory!")
    else:
        print("\n💀 The dragon defeated you! Game Over.")

battle()