
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


v = int(position[0]) - 1
h = int(position[1]) - 1
map[v][h] = "X"


print(f"{row1}\n{row2}\n{row3}")