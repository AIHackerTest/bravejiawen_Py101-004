
import sys
ten_things = "苹果 Oranges Crows Telephone Light Sugar"

print ("Wait there is not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')#函数split()，将一串字符串分裂成多个字符串组成的列表
more_stuff = ["Day", "Night", "Song", "Frisbee","Corn", "Banana", "Girl", "Boy"]
#当tenthinss字符串里还不等于10个字符时，从morestuff里取一个（可以用pop，也可以用.split()[0]??）
#加到tenthings里面，检查字符串长度，直到字符串达到10个。
while len(stuff) != 10:#不习惯用大于小于
	next_one = more_stuff.pop()#pop 弹出最后一个字符串
	print ("Adding: ", next_one)
	stuff.append(next_one)
	print ("There is %d items now." % len(stuff))

print ("stuff:", stuff)

print (stuff[0])#正数第一个元素
print (stuff[-1])#倒数第一个元素
print (stuff.pop())#弹出最后一个
print (' '.join(stuff))#Python join() 方法用于将序列中的元素以指定的字符（如空格，#）连接生成一个新的字符串。
print ('#'.join(stuff[3:5]))#3:5为stuff里序号为3到5的两个元素，包括头不包括尾，即第四个第五个。

