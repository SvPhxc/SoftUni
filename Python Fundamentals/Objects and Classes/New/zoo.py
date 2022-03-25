class Zoo:
    __animals = 0
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1
    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}")
        elif species == "fish":
            print(f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}")
        elif species == "bird":
            print(f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}")


zoo_name = input()
zoo = Zoo(zoo_name)

count = int(input())
for i in range(count):
    element = input().split(" ")
    species = element[0]
    name = element[1]
    zoo.add_animal(species, name)

species_type = input()
zoo.get_info(species_type)


# Great Zoo
# 5
# mammal lion
# mammal bear
# fish salmon
# bird owl
# mammal tiger
# mammal
