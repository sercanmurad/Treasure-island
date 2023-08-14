print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Be carefull!")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


first_step=input("Left or right ? Which way you choose\n")
first_step=first_step.lower()
if first_step=="left":
  second_step=input("Swim or wait the boat for the island?\n")
  second_step=second_step.lower()
  if second_step=="swim":
    print("Game over you eaten by crocodiles!")
  elif second_step=="wait":
    third_step=input("Which door you want to choose?\n Blue,Yellow or Red?")
    third_step=third_step.lower()
    if third_step=="red":
      print("Game over!")
    elif third_step=="blue":
      print("Game over!")
    elif third_step=="yellow":
      print("You choose the ride door!The last level is a historical question!")
      answer=input("In which year was Columbus discovers America! ")
      if answer == "1492":
        print("Right answer!You find the treasure.\n")
      else:
        print("You choose wrong answer!\nYou are falling in to the water!")
    else:
      print("You choose don\'t existing door.Game over!")
elif first_step=="right":
  print("Game over you fall!")