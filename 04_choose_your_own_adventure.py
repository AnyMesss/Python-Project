name = input("Type your name: ")
print(f"Welcome, {name}, to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go ?  ").lower()

if answer == "left":
  answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

  if answer == "swim":
    print("you swim across and were eaten by an alligato")
  elif answer == "walk":
    print("You walked for many kilometers, ran out of water and you lost the game")
  else:
    print("Not a valid option. you lose.")


elif answer == "right":
  answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

  if answer == "back":
    print("You go back and lose.")
  elif answer == "cross":
    answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

    if answer == "yes":
      print("You talk to the stanger and they give you gold, you WIN!")
    elif answer == "no":
      print("You ignore the stranger and they are offended ans you lose")

    else:
      print("Not a valid option. you lose.")
  else:
    print("Not a valid option. you lose.")
else:
  print("Not a valid option. you lose.")

print(f"Thank you for trying {name}")