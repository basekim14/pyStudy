# 20-03-02
# EX 34.6

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibers(self):
        print('티버: 피해량 {0}'.format(self.ability_power * 0.65 + 400))
        

health, mana, ability_power = map(float, input().split())

x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibers()
