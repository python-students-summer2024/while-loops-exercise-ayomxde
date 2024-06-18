def sing(starting_bottles):
    i = starting_bottles
    keep_looping = True
    while keep_looping:
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_looping = False
        i -= 1
