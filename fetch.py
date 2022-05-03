import math, random

class Roll:
    def __init__(self):
        pass

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.times_rolled = 0
    def roll(self):
        self.times_rolled += 1
        return math.ceil(random.uniform(0, self.sides))

class Pool:
    def __init__(self, size, difficulty, comment=""):
        self.size = size
        self.comment = comment
        self.difficulty = difficulty
        self.reroll_limit = 999
        self.dice = []
        for _ in range(size):
            self.dice.append(Dice(10))
        self.event_log = ["Initialized"]

    def roll(self):
        self.event_log.clear()
        rolls_to_make = [d for d in self.dice]
        successes = 0
        while len(rolls_to_make) > 0:
            next_dice = rolls_to_make.pop()
            result = next_dice.roll()
            if result >= self.difficulty:
                successes += 1
                self.event_log.append(f"{result} beats {self.difficulty}, success (rolled {next_dice.times_rolled} times)")
            else:
                self.event_log.append(f"{result} fails {self.difficulty}, failure (rolled {next_dice.times_rolled} times)")
            if result in self.reroll_triggers and next_dice.times_rolled < self.reroll_limit:
                self.event_log.append(f"rerolling a {result}")
                rolls_to_make.append(next_dice)
        self.event_log.append(f"######################################\n")
        self.event_log.append(f"{self.comment}\n")
        self.event_log.append(f"final result was {successes} successes")
        return successes

    def ten_again(self):
        self.reroll_triggers=[10]
        return self.roll()

    def nine_again(self):
        self.reroll_triggers=[10,9]
        return self.roll()
    
    def eight_again(self):
        self.reroll_triggers=[10,9,8]
        return self.roll()

    def rote(self):
        self.reroll_limit = 2
        self.reroll_triggers=[1,2,3,4,5,6,7]
        return self.roll()

    def __str__(self):
        output = ""
        for event in self.event_log:
            output += event
            output += "\n"
        return output

if __name__ == "__main__":
    pass