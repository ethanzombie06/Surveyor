class weapon:
    def __init__(self, damage, size, position):
        self.damage = damage
        self.size = size
        self.postion = position
    
    def damage_target(self, target):
        target.change_health(-self.damage)

class radar(weapon):
    def collides_with(self, target):
        distance = (self.postion - target.pos).length()
        return distance <= (self.size + target.size)