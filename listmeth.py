#1.Append()-The append() method appends an element to the end of the list.
veggies = ["cabbage", "tomato", "chilly"]

veggies.append("pumpkin")

print(veggies)
print("-----")
#2.The clear() method removes all the elements from a list.

veggies = ["cabbage", "tomato", "chilly"]

veggies.clear()

print(veggies)
print("-----")

#3.veggies = ["cabbage", "tomato", "chilly"]

x = veggies.copy()

print(x)
print("-----")
#4.The count() method returns the number of elements with the specified value.

veggies = ["cabbage", "tomato", "chilly"]

x = veggies.count("cherry")

print(x)
print("-----")

#5.Add the elements of a list (or any iterable), to the end of the current list

veggies = ["cabbage", "tomato", "chilly"]

cars = ['Ford', 'BMW', 'Volvo']

veggies.extend(cars)

print(veggies)
print("-----")

#6.The index() method returns the position at the first occurrence of the specified value.

veggies = ["cabbage", "tomato", "chilly"]

x = veggies.index("tomato")

print(x)
print("-----")

#7.The insert() method inserts the specified value at the specified position.

veggies = ["cabbage", "tomato", "chilly"]

veggies.insert(1, "pumpkin")

print(veggies)
print("-----")

#8.The pop() method removes the element at the specified position.

veggies = ["cabbage", "tomato", "chilly"]

veggies.pop(1)

print(veggies)
print("-----")

#9.The remove() method removes the first occurrence of the element with the specified value.

veggies = ["cabbage", "tomato", "chilly"]

veggies.remove("tomato")

print(veggies)
print("-----")

#10.The reverse() method reverses the sorting order of the elements.

veggies = ["cabbage", "tomato", "chilly"]

veggies.reverse()

print(veggies)
print("-----")

#11.The sort() method sorts the list ascending by default.

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)