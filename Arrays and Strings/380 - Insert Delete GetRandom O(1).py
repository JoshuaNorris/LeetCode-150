import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val not in self.list:
            return False
        else:
            index = self.dict[val]
            last_element = self.list[-1]

            self.list[index] = last_element
            self.dict[last_element] = index

            self.list.pop()
            del self.dict[val]

            return True

    def getRandom(self) -> int:
        random_integer = random.randint(0, len(self.list)-1)
        return self.list[random_integer]