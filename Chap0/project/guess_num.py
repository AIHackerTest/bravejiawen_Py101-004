
import random
key = random.randint(1,20)
def is_key_num(word):
    try:
        int(word)
        return True
    except ValueError:
        return False
    

print("一起来玩猜数字游戏吧！")
print("在1到20里猜一个数，你有十次机会")
print("你猜我们这次的数字是几？请输入数字：")
num1 = input()
a=is_key_num(num1)
while a==False:
    print("请确保输入的是数字~请重新输入")
    num1=input()
    a=is_key_num(num1)

num=int(num1)



for i in range(1,10):
    j = 10-i
    if num > key:#小于key就输出很遗憾，猜大一点吧
        print("比正确答案大，你还有%r次机会，请输入数字：" % j)
        num = int(input())
    elif num < key:
        print("比正确答案小，还有%r次机会，请输入数字：" % j)
        num = int(input())
    elif num == key:
        print("恭喜你答对了！正确答案是%r" % key)
        break
        
print("抱歉，你的机会用完了:(")