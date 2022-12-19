#Heroes Inventory 2.0 
#demonstrates tuples 


#create items wit a tuple and display using a for loop 
inventory = ("sword",
             "armor",
             "shield",
             "healing potion") 
print("Your items:")


for item in inventory: 
    print(item)


print("\n\n")
input("\t\t\t\t\'Enter'") 


#get length of tuple 
print("You have", len(inventory), "items in your heroes posession.") 


#test for membership with in 
if "healing potion" in inventory: 
    print("You will live to fight another day!") 


#display one item through an index 
index = int(input("\nEnter the index number for an item in inventory: ")) 
print("At index", index, "is", inventory[index]) 


#display slice
start = int(input("\nEnter the index number to begin a slice:")) 
finish = int(input("Enter the index number to end the slice:")) 
print("inventory[", start, ":", finish, "] is", end=" ") 
print(inventory[start:finish]) 


print("\n\n")
input("\t\t\t\tPress 'Enter' to continue.") 


#concetenating two tuples 
chest = ("gold", "gems")
print("You find a chest and it contains: ")
print(chest)
print("You add the", chest[0], "and", chest[1], "from the chest to your inventory")
inventory += chest 
print("\nYou now have", len(inventory), "items in your inventory.")
print(inventory) 


myList = list(inventory)
myList.remove(chest[0])
print("\nSuddenly a wild Gayden appears and bums the gold off of you.")


print("\nYour inventory is now", myList,)


print("\n\n")
input("\t\t\t\t\tPress 'Enter' to exit.")