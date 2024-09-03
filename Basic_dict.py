marks = {"Soumya": 90, "Mithun": 80, "Hitesh": 70}

print("\nPrinting Names:")
for name in marks:
    print(name)

print("\nPrinting Name's mark:")
for name in marks:
    print(marks[name])

print("\nPrinting the Mark:")
for mark in marks.values():
    print(mark)

print("\nPrinting the Name And Mark: ")
for name, mark in marks.items():
    print(f"Name: {name}, Mark: {mark}")

print("\nUnpacking the datas: ")
name1, name2, name3 = marks
print(name1)
print(name2)
print(name3)

mark1, mark2, mark3 = marks.values()
print(mark1)
print(mark2)
print(mark3)


print("\nAuto Formating: ")

sells_record = {
    "Item": "Books",
    "Price": 102,
    "Numbers": 5,
    "person": "Soumya"
}

My_String = '{} has bought {} {} in a total price of {}'

F_String = My_String.format(sells_record['person'], sells_record['Numbers'], sells_record['Item'], sells_record['Price']*sells_record['Numbers'])
print(F_String)

F_String2 = f"{sells_record['person']} has bought {sells_record['Numbers']} {sells_record['Item']} for His Child."
print(F_String2)
