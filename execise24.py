import copy 

produtos = [
    {"name" : " product 5" , "price" : 50.0},
    {"name" : " product 1" , "price" : 85.0},
    {"name" : " product 2" , "price" : 52.0},
    {"name" : " product 4" , "price" : 10.0},
    {"name" : " product 3" , "price" : 20.0},
]

new_product =[
    {**p, "price": round(p["price"]*1.1 , 2)}
    for p in copy.deepcopy(produtos)
] 

produtos_rodenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p["name"],
    reverse= True
)

produtos_rodenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p["price"]

)


print(*produtos, sep= "\n")
print()
print(*new_product, sep= "\n")
print()
print(*produtos_rodenados_por_nome, sep= "\n")
print()
print(*produtos_rodenados_por_preco, sep= "\n")




