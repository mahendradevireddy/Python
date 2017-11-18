from classes.game import Person, bcolors



magic=[{"Name":"Fire","cost":10,"dmg":60},
       {"Name": "Thunder", "cost": 10, "dmg": 80},
       {"Name": "Blizzard", "cost": 10, "dmg": 70}]

player=Person(460,65,60,34,magic)
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
