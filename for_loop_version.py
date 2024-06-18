def sing(starting_bottles):
    for i in range(starting_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")