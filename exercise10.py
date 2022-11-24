name = input("type your name ")

index = 0 
new_name = " "

while index < len(name):
    letter = name[index]
    new_name += f"*{letter}"
    index += 1


new_name += "*"
print(new_name)
