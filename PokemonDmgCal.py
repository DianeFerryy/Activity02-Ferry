import random
level = 90
attack = 205
defense = 188
power = 110

target = 1
weather = 1
badge = 1
critical = 1
random = round(random.uniform(0.85,1.0),2)
stab = 1.5
type = 0.5
burn = 1
modifier = target*weather*badge*critical*random*stab*type*burn*1

damage = ((2*level)/5)+2
damage = (damage*power)*(attack/defense)
damage = ((damage/50)+2)*modifier

print(round(damage))
print("Random Number = "+str(random))