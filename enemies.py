class enemy:
    def __init__(self,health,initial_pos,size=10):
        self.health = health
        self.pos = initial_pos
        self.size = size

    def change_health(self, damage):
        self.health += damage
    def change_pos(self, x, y):
        self.pos.x += x
        self.pos.y += y