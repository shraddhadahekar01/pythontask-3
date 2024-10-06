#1.The clear() method removes all the elements from a dictionary.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
college_data.clear()
print(college_data)

#2.The copy() method returns a copy of the specified dictionary.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
college_data.copy()
print(college_data)

#3.The fromkeys() method returns a dictionary with the specified keys and the specified value.

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)


print(thisdict)

#4.The get() method returns the value of the item with the specified key.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
x = college_data.get("section")
print(x)

#5.The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
x = college_data.items()
college_data["branch"] = 2024
print(x)

#6.The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
x = college_data.keys()
print(x)

#7.The pop() method removes the specified item from the dictionary.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
college_data.pop("branch")
print(college_data)

#8.The popitem() method removes the item that was last inserted into the dictionary. 
college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
college_data.popitem()
print(college_data)

#9.The setdefault() method returns the value of the item with the specified key.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
x = college_data.setdefault("section","C")
print(x)

#10.The update() method inserts the specified items to the dictionary.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
college_data.update({"grade":"A"})
print(college_data)

#11.The values() method returns a view object. The view object contains the values of the dictionary, as a list.

college_data= {
  "branch": "electronics",
  "section": "B",
  "batch": 2024
}
x=college_data.values()
print(x)
