class enemy:
    def __init__(self,health,initial_pos):
        self.health = health
        self.pos = initial_pos

    def change_health(self, damage):
        self.health += damage
    def change_pos(self, x, y):
        self.pos.x += x
        self.pos.y += y