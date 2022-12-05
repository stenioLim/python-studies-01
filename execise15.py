import os

list_1 = []
while True:
    print("Select the option")
    option = input("[i]insert, [l]list, [d]delete ")
    if option == "i":
        os.system("clear")
        product = input("enter the product")
        list_1.append(product)

# block responsible for delete a selected index from the list
    elif option == "d":
        index_str =input("select product for delete:")
        try:
            index_2 = int(index_str)
            del list_1[index_2]
        except ValueError:
            print("Enter an integer")
        except IndexError:
            print("Cloud not find this product")
        except Exception:
            print("error not found")


# block responsible for listing the products on the list_1

    elif option == "l":
        os.system("clear")

        if len(list_1) == 0: 
            print("nothing to list")

        for i, product in enumerate(list_1):
            print(i, product)
        
    else:
            print("enter the option i, a or d")    