treasure_island = '''
********************************Welcome to Treasure Island********************************
    ___
    ).x)
   (:_(
  
  Finrod




                                                                      



         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /
   '''
print(treasure_island)
print("Your mission is to find a Treasure")
input1 = input("do you want to go LEFT or RIGHT...Enter 'L' for left and 'R' for right")
if input1.upper() == "R":
    print("YOU FELL INTO THE HOLES ***GAME OVER***")
elif input1.upper() == "L":
    input2 = input("Would you like to WAIT or GO for a SWIM...ENTER 'W' for wait and 'G' for swim")
    if input2.upper() == "G":
        print("YOU ARE BEING ATTACKED BY TROUT ***GAME OVER***")
    else:
        input3 = input("While you're waiting for the door to open please chose the color R for red, Y for Yellow & Blue for B")
        if input3.upper() == "Y":
            print("CONGRATULATIONS YOU WIN!!!")
            print(treasure_island)
        elif input3.upper() == "B":
            print("YOU ARE EATEN BY A BEAST...GAME OVER!!!")
        elif input3.upper() == "R":
            print("YOU ARE BURNED BY A FIRE...GAME OVER!!!")
        else:
            print("GAME OVER!!!")
else:
    print("GAME OVER!!!")