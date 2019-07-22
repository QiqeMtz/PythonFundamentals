print("1st loop:")

for name in "John", "Sam", "Luis":
    print("Hello " + name + "\n")

print("\n2nd loop with defined range:")

for i in range(10, 30):
    print(i)

print("\n3rd loop with only given a sequence")
for i in range(10):
    print(i)

print("\n4th loop")
total  = 0
for i in 5,6,11,13:
    print(i)
    total = total + i

print(total)

# this is a comment
print("\n5th loop")
print("I dont care about the i value in the loop, i just need to repeat x times an action")
for _ in range(10):
    print("Hello")

for i in range(0,15,3):
    print(i)

for i in range(1000,10,-10):
    print(i)

names = ["John", "Luis", "Sam"]

for name in names:
    print(name)

name = names[0]

for letter in name:
    print(letter)

# Nested loop
nums = [1,2,3]
letters = ['a', 'b', 'c']

for num in nums:
    for letter in letters:
        print(str(num) + letter)

# Iterate over list of lists

lists = [ ['1','2','3'], ['a','b','c'], ['+','-','='] ]

for list in lists:
    print(list)

for list in lists:
    for item in list:
        print(item)