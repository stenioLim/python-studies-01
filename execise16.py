# cpf 477.233.043-74


##input_cpf = input("CPF [477.233.043-74]:")

cpf = "54120826295"



nine_digits = cpf[:9]
regressive_counter_1 = 10 

result = 0

for digits in nine_digits:
    result += int(digits) * regressive_counter_1
    regressive_counter_1 -= 1 
digits_1 = (result * 10) % 11
digits_1 = digits_1 if digits_1 <= 9 else 0
##print(digits_1)


ten_digits = nine_digits + str(digits_1)
regressive_counter_2 = 11

result_2 = 0
for digits in ten_digits:
    result_2 += int(digits) * regressive_counter_2
    regressive_counter_2 -= 1
digits_2 = (result_2*10)%11
digits_2 = digits_2 if digits_2 <= 9 else 0
##print(digits_2)

cpf__calculated = f"{nine_digits}{digits_1}{digits_2}"

if cpf == cpf__calculated:
    print(f"cpf:{cpf} its valid ")
else: 
    print("cpf invalid")