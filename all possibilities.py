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

place = 0

for name, code in guide_list.items():
    for size_option in ("S", "M", "L"):
        for jungle_option in ("R", "L"):
            if jungle_option == "L":
                if size_option == "S":
                    aether_location = 3800 - ((3800-3276) * code)
                elif size_option == "M":
                    aether_location = 6000 - ((6000-4992) * code)
                elif size_option == "L":
                    aether_location = 8000 - ((8000-6552) * code)
            elif jungle_option == "R":
                if size_option == "S":
                    aether_location = 3276 + ((3800-3276) * code)
                elif size_option == "M":
                    aether_location = 4992 + ((6000-4992) * code)
                elif size_option == "L":
                    aether_location = 6552 + ((8000-6552) * code)
            place += 1
            print()
            print(f"\033[31mNumber {place}:\033[0m")
            print("\033[32m!!!!World Info!!!!\033[0m")
            print(f"Name: {name} | Size: {size_option} | Jungle side: {jungle_option} | Code: {code}")
            print()
            print("\033[32m!!!!Aether/Shimmer Location!!!!\033[0m")
            print(f"{aether_location}" + " West" if jungle_option == "L" else f"{aether_location}" + " East") 
            print()
            print("\033[34m----\033[0m")
        