def zipper(list_1, list_2):
    time_max = min(len(list_1),len(list_2))
    return[(list_1[i], list_2[i]) for i in range(time_max)]

l1 = ["Salvador", "Ubatuba", 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))
print()
print(list(zip(l1,l2)))