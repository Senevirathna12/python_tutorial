# In Python, we can store multiple data types in a single list, but usually, we keep only one data type in a list.

names = ["Amith" , "Chamara" , "Jhone", "Lissa", "Alice"]
print(names)

names.append('Kamal')
print(names)

names.pop(-1)
print(names)

names.insert(0,"Kamal")
print(names)

names[0] = "Anuk"
print(names)

print ('Ammount of element :' + str(len(names)))