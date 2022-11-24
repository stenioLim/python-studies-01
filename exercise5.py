name = input("type your name: ")
old = input("type your old: ")

if name and old:
    print(f"{name}")
    print(f"{name}"[::-1])
    if " " in name:
        print("you name has space ")
    else:
        print("your name has no space ")
    print(f"your name has {len(name)} letters")
else:
    print("write to redo")