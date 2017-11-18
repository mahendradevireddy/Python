
class Enemy:
    hp=200 #static variable

    def __init__(self,atkl,atkh):
        self.atkl=atkl #dynamic variable
        self.atkh=atkh

    def gtk(self):
         print(self.atkl)


    def gethp(self):
        print(self.hp)


'''enemy1=Enemy(40,50)
enemy1.gtk()
enemy1.gethp() #accesing variable through method
print(enemy1.hp) #accesing variable directly'''
