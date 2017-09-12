people = 30
cars = 40
buses = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we can't decide")	
	
if buses > cars and buses < people:
    print("let's take the bus")
elif buses < cars and buses < people:
    print("let's take the cars.")
else:
    print ("we can't decide")    