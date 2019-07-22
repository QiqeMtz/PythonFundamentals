# Define original dictionary
usernames = {"Sammy":"sammy-shark", "Jamie":"mantisshripm54"}

# Set up while loop to iterate

while True:
    # Request user to enter a name
    print("Enter a name:")

    # Assign name to a variable
    name = input()

    # Check if name is in the dictionary and print feedback
    if name in usernames:
        print(usernames[name], "is the username of", name)
    
    # if name isnt in the dictionary
    else:
        print("I dont have " + name + "s username, what is it?")

        #take new username for the provided name
        username = input()

        # Assign username to name key
        usernames[name] = username

        # Print feedback
        print("Data updated!")