x = 3
a = "gorillas"
t = True

item_1 = "milk"
item_2 = "cheese"
item_3 = "bread"

shopping_list = []
shopping_list.append(item_1)
shopping_list.append(item_2)
shopping_list.append(item_3)

for item in shopping_list:
    print(item)

#dictionary
foods = {}

foods["banana"] = "A delicious and tasty treat!"
foods["dirt"] = "Not delicious. Not tasty. DO NOT EAT"
   
if "banana" in foods:
    print("Cheese is one of the known foods!")
    print(foods["banana"])

#add list to dictionary
ingredients = {}
ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]

#add dictionary to list
europe = []
germany = {"name" : "Germany", "population" : 8100000}
europe.append(germany)

luxembourg = {"name" : "Luxembourg", "population" : 5120000}
europe.append(luxembourg)

for item in europe: 
    print(item)
