# Unordered collection of items
# Maps a key to a value (key,value)
# Good for store values in Python
# Retrieve values when we know the key
# Made with curly braces {}
# Do not mantain order or the ability to be indexed
# Dictionaries are mutable

sammy = {"username":"sammy-shark", "online":True, "followers":987}
print(sammy)

# Left -> keys and right -> values
# Keys can compromise any immutable data type and in the dictionary above
# values can consist of any data type

# Accessing data items using keys
print(sammy["username"])

# Accessing elements with functions
# dict.keys() isolate keys
# dict.values() isolate values
# dict.items() return items in a list format of key,value tuple pairs

print(sammy.keys())
print(sammy.values())
print(sammy.items())

# Query across dictionaries
sammy.clear()
sammy = {"username":"sammy-shark", "online":True, "followers":987}
jesse = {"username":"jesse-1", "online":False, "points":723}

for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])

# Print all related keys with their values
for key, value in sammy.items():
    print(key, "is the key of the value:", value)

# Modifying a dictionary
usernames = {"Sammy":"sammy-shark", "Jamie":"mantisshrimp54"}
usernames["Drew"] = "squidly"
print(usernames)

drew = {"username":"squidly", "online":True, "followers":305}
drew["followers"] = 315

print(drew)

jesse.clear()

jesse = {"username":"jesse-1", "online":False, "points":723}
jesse.update({"followers":481})
print(jesse)

sammy.update({"online":False})
print(sammy)
sammy["online"]=True
print(sammy)

del sammy["online"]
print(sammy)