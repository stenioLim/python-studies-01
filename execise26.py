list_a = [ 1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

list_sum = []
for i in range(len(list_b)):
    list_sum.append(list_a[i] + list_b[i])
print (list_sum)


list_sum = [
    x + y for x ,y in zip(list_a,list_b)
]

print(list_sum)