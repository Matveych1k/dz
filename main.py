from random import randint

class Randomizer:
    def __init__(self, begin_num=0, end_num=0):
        self.begin_num = begin_num
        self.end_num = end_num

    def generate(self, begin_num, end_num):
        self.begin_num = begin_num
        self.end_num = end_num
        return randint(self.begin_num, self.end_num)

randomizer = Randomizer()

random_number = randomizer.generate(10, 50)

print(f"Випадкове число між {randomizer.begin_num} та {randomizer.end_num}: {random_number}")