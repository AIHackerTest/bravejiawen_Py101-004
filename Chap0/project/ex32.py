
hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges','pears','apricots']
change = [1,'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print("This is count %d " % number)

for fruit in fruits:
	print("A fruit of type: %s" % fruit) 

for i in change:
	print("I got %r " % i) 

elements = range(0,6)#直接赋值一个列表，或者使用下面的方式



for i in elements:
	print("Element was: %d" % i)