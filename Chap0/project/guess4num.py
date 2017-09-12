'''
开发升级版猜数字小游戏，实现以下功能：
程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
用户输入 4 位数进行猜测，程序返回相应提示
用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
用户猜测后，程序返回 A 和 B 的数量
比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
猜对或用完 10 次机会，游戏结束
'''
import random
def true_num():
    '''制造一个随机四位数，先生成一个列表，然后用列表生成数字'''
    num = random.sample(range(0,10),4)
    if num[0] == 0:
	    num[0],num[1] = num[1],num[0]
    return ''.join(str(i) for i in num)

def com_num(num0,g_num):
    '''对比两个数字，先把数字转化成字符串，然后逐个去对比，最后返回结果'''
    count_a = count_b = 0
    for i in range(4):
        if g_num[i] == num0[i]:
            count_a += 1
        elif g_num[i] != num0[i] and g_num[i] in num0:
            count_b += 1
    return count_a,count_b

def guess():
    '''主程序，计数，猜数'''
    num0 = true_num()
    n = 10
    print('我心里想了一个四位数，由不同的四个数字组成，猜猜看吧！')
    while n>0:
        g_num = input('输入4位数字>')
        if g_num.isdigit() and len(g_num) == 4:
            a,b = com_num(num0,g_num)
            if a == 4:
                exit('恭喜你，答对啦！')
            else:
                print('你猜的结果为:%dA%dB,come on！' % (a,b))
            n -= 1
			print('你现在还有%d次机会' % n)
        else:
            print('麻烦输入一个四位数啦')
		
    print('游戏结束啦，正确答案为：%d' % int(num0))
guess()
