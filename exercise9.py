frist_name = input("Type your name: ")

num_letters = int(len(frist_name))


if num_letters <= 4:
    print("your name is small")
elif num_letters == 5 or num_letters == 6 :
    print("your name is normal")
elif num_letters > 6:
    print("your name is big")
else:
    print("enter a name greater than 1")
