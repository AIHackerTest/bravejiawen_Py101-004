def add(a,b):
    print("adding %d + %d" % (a,b))
    return a + b
	
def substract(a, b):
    print("substracting %d - %d" %(a, b))
    return a-b
	
def multiply(a, b):
    print("multiplying %d * %d" % (a, b))
    return a * b
	
print("do some math")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)

print("age:%d, height:%d,weight:%d" %(age, height, weight))

print("here is the puzzle:")

what = add(age, substract(height, multiply(weight,2)))
print(what)
