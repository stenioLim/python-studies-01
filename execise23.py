def sum_1(x,y):
    return x + y
    
def multiply( x, y):
    return x * y

def create_func (function, x): 
    def inter(y):
        return function(x ,y) 
    return inter

sum_whit_five = create_func(sum_1, 5)
multiply_for_ten = create_func(multiply, 10)

print(sum_whit_five(10))
print(multiply_for_ten(10))