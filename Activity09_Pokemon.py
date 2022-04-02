from logging import critical
import random 

Pmtype = str(input("Pokemon Type: "))
Chalevel = int(input("Charizard Level: "))
SAttack = int(input("Special Attack: "))
Stype = str(input("Skill Type: "))
Pwr = int(input("Power: "))
FerLevel = int(input("Feraligatr's Level: "))
SDef = int(input("Special Defense: "))
Etype = str(input("Enemy Type: "))
Gen = int(input("Generation: "))
Wthr = str(input("Weather: "))
Trgt = int(input("Target: "))

def modifier (Trgt, Wthr, Gen, Pmtype, Stype, Etype):

#TARGET

    if Trgt == 1:
        Trgt = 1
    else:
        Trgt = .5

#WEATHER
    if Wthr == "beneficial":
        Wthr = 1.5
    if Wthr == "against":
        Wthr = .5
    if Wthr == "otherwise":
        Wthr = 1

#BADGE
    if Gen == "2":
        Gen = 1.25
    else:
        Gen = 1
    
#CRITICAL
    critic = [1 , 2]
    critica = random.choice(critic)
    if critica == 2:
        print("\n CRITICAL HIT")
    else: 
        print("HIT")

#RANDOM
    randm = [0.85,1]
    rndm = random.choice(randm)

#STAB
    if Pmtype == "fire" and Stype == "fire":
        effect3 = 1.5
    else:
        effect3 = 1

#TYPE
    if Stype =="fire" and Etype == "fire":
        effect1 = .5
    if Stype =="fire" and Etype == "water":
        effect1 = .5
    if Stype =="fire" and Etype == "steel":
        effect1 = 2
    if Stype =="fire" and Etype == "rock":
        effect1 = .5
    if Stype =="fire" and Etype == "grass":
        effect1 = 2
    if Stype =="fire" and Etype == "bug":
        effect1 = 2
    if Stype =="fire" and Etype == "dragon":
        effect1 = .5
    if Stype =="fire" and Etype == "ice":
        effect1 = 2
    if Stype =="fire" and Etype == "normal":
        effect1 = 1
    if Stype =="fire" and Etype == "flying":
        effect1 = 1
    if Stype =="fire" and Etype == "poison":
        effect1 = 1
    
    type = effect1

    if type <=.5:
        print ("NOT EFFECTIVE!!")
    if type >=2:
        print("SUPER EFFECTIVE!!")
    else:
        type == 1
        
#OTHER
    other = 1

#BURN
    burned = [.5 , 1]
    brn = random.choice(burned)
    if brn == .5:
        print("\n The Attacker is BURNED!")

#CALCULATION FOR MODIFIER
    mod = Trgt * Wthr * Gen * critica * rndm * effect3 * type * other * brn
    return mod
    
#CALCULATION FOR DAMAGE
dmge = ((((((2*Chalevel)/5)+2)* Pwr * SAttack/SDef)/50)+2) * modifier(Trgt, Wthr, Gen, Pmtype, Stype, Etype)
print("CHARIZARDS DAMAGE TO FERALIGATR :", dmge)
