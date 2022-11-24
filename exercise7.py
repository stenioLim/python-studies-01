## odd or even 

num = input("type your number ")
num_int = int(num)
num_math = int(num_int % 2) # modulo operator (%)
if num_math == 0 :
    print("even")
else:
    print("odd")
