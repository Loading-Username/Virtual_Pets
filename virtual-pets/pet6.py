class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " says 'Mmmmmm, so good and tasty!'")
        else:
            print(self.name + " is too ded to eat.")
            
    def sleep(self):
        print("I'm schleeep")
        
    def play(self):
        print("Yeet!")
        
    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " attacks " + other.name +"!")
        print(other.name + " goes 'oof' and dies.")
        other.is_alive = False

    def hug(self, other):
        print(self.name + " hugs " + other.name +"!")
        other.happiness += 1
        print(other.name + " says, 'I'm like " + str(other.happiness) + " happy now.")

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"

    def hunt_wabbits(self, other):
        print(self.name + " has gone hunting for wabbits!")
        self.happiness += 1
        print(self.name + " is getting happier!")
    
pet1 = Pet("Elmer Fudd")
pet2 = Pet("Bugs Bunny")
pet3 = Pet("Yosemite Sam")
