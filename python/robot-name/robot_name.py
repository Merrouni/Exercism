import random,string

class Robot(object):
    namesRegistery = []
    def __init__(self):
        self.generateName()

    def reset(self):
        Robot.namesRegistery.remove(self.name)
        self.generateName()

    def generateName(self):
        self.name = Robot.randomName()
        while self.name in Robot.namesRegistery:
            self.name = Robot.randomName()
        Robot.namesRegistery.append(self.name)
        
    def randomName():
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + ''.join(random.choice(string.digits) for _ in range(3))
