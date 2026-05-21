import os
import time
print("--- Terraria aether biome finder ---")

# Dictionary of guide names:code
# i asked chatgpt to fill in the names in a dictionary, it would have been very
# time consuming to do it myself. this is the correct way to use AI
# i checked it to make sure its correct
guide_list = {
    "Joe":     0.0000,
    "Connor":  0.0278,
    "Tanner":  0.0556,
    "Wyatt":   0.0833,
    "Cody":    0.1111,
    "Levi":    0.1389,
    "Luke":    0.1667,
    "Jack":    0.1944,
    "Scott":   0.2222,
    "Logan":   0.2500,
    "Cole":    0.2778,
    "Asher":   0.3056,
    "Bradley": 0.3333,
    "Jacob":   0.3611,
    "Garrett": 0.3889,
    "Dylan":   0.4167,
    "Maxwell": 0.4444,
    "Steve":   0.4722,
    "Brett":   0.5000,
    "Andrew":  0.5278,
    "Harley":  0.5556,
    "Kyle":    0.5833,
    "Jake":    0.6111,
    "Ryan":    0.6389,
    "Jeffrey": 0.6667,
    "Seth":    0.6944,
    "Marty":   0.7222,
    "Brandon": 0.7500,
    "Zach":    0.7778,
    "Jeff":    0.8056,
    "Daniel":  0.8333,
    "Trent":   0.8611,
    "Kevin":   0.8889,
    "Brian":   0.9167,
    "Colin":   0.9444,
    "Jan":     0.9722
}


time.sleep(1)
# Help section

help = "Not Defined"
while not help == "C":
    help = input("Enter H to get help instructions, G to get Guide names dictionary, C to continue: ").upper()
    if help == "H":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("UPD: Image no longer needed, as of i added all guide names:codes in a dictionary")
        print("Check it")
        print("First, look at the guide name and find your first guide name.")
        print("Your guide died before? make a new world with the same seed")
        print("and check the guide name")
        print("---")
        input("press anything to continue reading...")
        print("---")
        print("Second, check where your jungle is. Shimmer/aether biome")
        print("always spawns on the same side of the jungle")
        print("---")
        input("press anything to continue reading...")
        print("---")
        print("Third, Check your world size, Small, Medium, Large.")
        time.sleep(1)
        print("Checked everything? we will continue with the program then")
    elif help == "G":
        for name, code in guide_list.items():
            print(f"{name:7} : {code}")
    else:
        pass

# guide name input
guide_name = input("Enter your guide name: ").capitalize()
if guide_name in guide_list:
    print("Successful!")

# if its incorrect VVV
else:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{guide_name} is not a valid guide name!")
        guide_name = input("Enter your guide name: ").capitalize()
        if guide_name in guide_list:
            break

guide_code = guide_list.get(guide_name) # assign code to this variable
print(f"Your guide name is: {guide_name}")
print(f"Your guide code is: {guide_code}")

# jungle input
world_jungle_side = input("Enter Jungle side, (L)eft, (R)ight: ").upper()

# if its incorrect VVV
while world_jungle_side != "R" and world_jungle_side != "L":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{world_jungle_side} is not a valid side! (L or R)")
    world_jungle_side = input("Enter Jungle side, (L)eft, (R)ight: ").upper()
os.system('cls' if os.name == 'nt' else 'clear')

# world size input
world_size = input("Enter World Size, (S)mall, (M)edium, (L)arge: ").upper()

# if its incorrect VVV
while world_size != "S" and world_size != "M" and world_size != "L":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{world_size} is not a valid size! (S or M or L)")
        world_size = input("Enter World Size, (S)mall, (M)edium, (L)arge: ").upper()
os.system('cls' if os.name == 'nt' else 'clear')

# calculation and output
if world_jungle_side == "L":
    if world_size == "S":
        aether_location = 3800 - ((3800-3276) * guide_code)
    elif world_size == "M":
        aether_location = 6000 - ((6000-4992) * guide_code)
    elif world_size == "L":
        aether_location = 8000 - ((8000-6552) * guide_code)
elif world_jungle_side == "R":
    if world_size == "S":
        aether_location = 3276 + ((3800-3276) * guide_code)
    elif world_size == "M":
        aether_location = 4992 + ((6000-4992) * guide_code)
    elif world_size == "L":
        aether_location = 6552 + ((8000-6552) * guide_code)
print(f"Your Aether coordinates is: {aether_location}")

# credits
time.sleep(4)
print("Credits VVVV:")
time.sleep(1)
print("Credits to Terrasteel for the formula")
print("mhykhol for discovering the correlation")
print("Unftf for discovering RNG numbers")
print("Terraria Speedrunners! and affiliated members for aiding")
print("Jasonthe4th for Infographics")
print("manwiththeafro for Infographics")
time.sleep(1)
input("Press any key to leave...")