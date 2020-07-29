foods = ["burger", "pizza", "steak"]
# index =  0(-3)    1(-2)     2(-1)

drinks = ["soda", "juice", "tea", "milk tea", "coffee"]

numbers = [5, 11, 14, 21, 42, 23, 5]

# any data type can be put into an array, and to make an array we use []

print(foods)
# prints whole array

print(foods[0])
# outputs burger

print(foods[-1])
# outputs steak

print(drinks[2:])
# prints anything after index number 2 inclusive

print(drinks[1:3])
# prints anything between index number 1 and 3 inclusive of 1(bottom value)

drinks[1] = "water"
# replaces value at index position 1  with specified value

foods.append("fries")
# adds another element at the end of the list

print(foods.index("pizza"))
# check index of element in list, if not in list, return error

print(foods)

foods.extend(drinks)
# adds drinks list to foods

print(foods)

numbers.insert(2, 37)
# adds a new element in specified index number, in this case, 2

print(numbers)

numbers.remove(42)
# removes a certain element from the list

numbers.pop()
# removes last element

print(numbers)

print(numbers.count(5))
# check how many of an element there is in a list

print(foods.sort())
# sorts a list in alphabetical order

print(foods.reverse())
# reverses order of a list

num = numbers.copy()
# copies a list

print(num)

drinks.clear()
# removes everything in the list
