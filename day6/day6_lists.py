# Create and Access Lists
print("Create and Access Lists------------------------------------------")
nameList = [
    "praful",
    "prem",
    "om",
]

print(nameList[0])
print(nameList[1])
print(nameList[2])

# Update List Items
print("Update List Items------------------------------------------")
nameList = [
    "praful",
    "prem",
    "om",
]

nameList[0] = "patnecha praful"

print(nameList[0])

print("Add Items------------------------------------------")

fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1,"orange")
print(fruits)

print("Remove Items------------------------------------------")
fruit = ["apple", "banana", "mango", "orange"]

fruit.remove("mango")
fruit.pop(1)
print(fruit)

# Loop through Lists
print("Loop through Lists------------------------------------------")

tasks = ["Wake up", "Study", "Exercise"]

for task in tasks:
    print("Task:", task)

# List Length & Sorting
print("List Length & Sorting------------------------------------------")

numsList = [5,4,1,6,3,2]

print("Length : ",len(numsList))

numsList.sort()
print("Sorted : " ,numsList)

numsList.reverse()
print("Reversed : ",numsList)

# Slicing (Partial List)
print("Slicing (Partial List)------------------------------------------")

fruits = ["apple", "banana", "mango", "orange", "grapes"]
print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])
