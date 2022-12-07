def odd_even (num):
    mult =  num % 2 == 0 

    if mult:
        return f"{num_1} is odd"
    return f"{num_1} is even"

num_1 = int(input("Enter the number for verification: "))

print(odd_even(num_1))