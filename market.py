market
def begin():
...     print("You walk into a market with about $150, considering the insane prices of food nowadays")
...     print("A stall lady greets you warmly")
...     print("She says,'Hello! Here's the stock!'")
...     money = 150
...     apple = 10
...     banana = 8
...     orange = 6
...     micar =  11
...     egg = 10
...     st = "10_apples_$4 8_bananas_$5 6_oranges_$3 10_milk_cartons_$11 9_Dozens_of_eggs_$10"
...     w = st.split()
...     for word in w:
...         print(word.lower())
...     choice = input("what would you like? (Type with out's'and purchase type of 1 item at a time and type 'milk_cart\
on')").lower().strip()
...     if choice == "apple":
...         quant = int(input("How many?"))
...         applep = quant * 4
...         if apple < quant:
...             print("Oh sorry, I don't have that many in stock..")
...         elif apple >= quant:
...             print(applep)
...             if money < applep:
...                 print("Sorry not enough money, comeback when you can!")
...             elif money >= applep:
...                 print("Here you go!")
...                 print(money - applep)
...                 print(apple - quant)
...     if choice == "banana":
            quant1 = int(input("How much?"))
...         bananap = quant1 * 5
...         if banana < quant1:
...             print("You're asking for too many...")
...         elif banana >= quant1:
...             print(bananap)
...             if money < bananap:
...                 print("Ohhh... well it's fine!")
...             elif money >= bananap:
...                 print("There you go!")
...                 print(money - bananap)
...     if choice == "orange":
...         quant2 = int(input("How many?"))
...         orangep = quant2 * 3
...         print(orangep)
...         if orange < quant2:
...             print("Uhh too many oranges at once")
...         elif orange >= quant2:
...             print(orangep)
...             if money < orangep:
...                 print("Not enough money")
...             elif money >= orangep:
...                 print("Here's your oranges")
...                 print(money - orange)
...     if choice == "milk_carton":
...         quant3 = int(input("How many?"))
...         mcp = quant3 * 11
...         print(mcp)
...         if micar < quant3:
...             print("I don't have that many cartons")
            elif micar >= quant3:
...             print("Do you have enough")
...         if money < mcp:
...             print("Sorry to say but you don't have enough")
...         elif money >= mcp:
...             print("There you go!")
...             print(money - mcp)
...     if choice == "egg":
...         quant4 = int(input("How many?"))
...         eggp = quant4 * 10
...         print(eggp)
...         if egg < quant4:
...             print("Y'know I don't have that many.. right?")
...         elif egg >= quant4:
...             print("Don't drop any!")
...             print(money - eggp)
...     else:("If you don't want anything just leave")