
from pgzero.actor import Actor

class CarImage():
    def __init__(self):
        self.car_image = 1 #pygame.image.load("photo/others/lawnmower.gif").convert_alpha()


class Car(Actor):
    def __init__(self,L):
        Actor.__init__(self,"others/lawnmower.gif")

        #self.image = image.car_image
        #self.rect = self.image.get_rect()
        self.left = - self.width
        self.L = L
        self.active = False
        self.speed = 4
        #self.mask = pygame.mask.from_surface(self.image)

    def move1(self):
        if self.right < self.L:
            self.left += self.speed
        else:
            self.right = self.L + 4

    def move2(self):
        self.left += self.speed