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