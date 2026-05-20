#QUESTION 1: CREATING AND MODIFYING LISTS
fruitlist =["apple", "rasberryy", "strawberry", "tomato"]
fruitlist.append("pinapple")
fruitlist.insert(0,"blueberry")
fruitlist.remove("tomato")
print(fruitlist)

#QUESTION 2: List Operations
originalnumblist =[1, 2, 3, 4, 5]
secnumblist = [1, 4, 9, 16, 25]
total_sum = sum(originalnumblist)
avarage = sum(originalnumblist)/len(originalnumblist)
print(originalnumblist)
print(secnumblist)
print(total_sum)
print(avarage)

#Question 3: Dictionary operations
country_capitaldict = {
"Spain": "Madrid",
"Japan": "Tokyo",
"France": "Paris",
"Italy":"Milan"
}
country_capitaldict["Egypt"]="Cairo"
country_capitaldict["Italy"]= "Barcelona"
del country_capitaldict["Italy"]
print(country_capitaldict)

#Question 5: Dictonary Operations
fruit_coloursdict ={
  "Apple": "Green",
  "Grapes": "Purple",
  "Pinapple": "Yellow",
  "Blueberry": "Blue"
  } 
keys = fruit_coloursdict.keys()
print(keys)
values = fruit_coloursdict.values()
print(values)
print(fruit_coloursdict)
fruit = input("Enter a fruit name")

if fruit in fruit_coloursdict:
  print(f" the {fruit} exists in dictionary and colour is {fruit_coloursdict[fruit]} ")
else:
  print("error {fruit} not found")
