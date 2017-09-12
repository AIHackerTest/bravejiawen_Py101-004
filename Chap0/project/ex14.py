
from sys import argv 
#import ...:导入模块，from ... import... 从模块中导入指定部分，
#from ...import * ,把模块中的部分全部导入到当前命名空间


script, user_name=argv
prompt = '> '

print ("hi %s, i am the %s script." %(user_name,script))
print ("i'd like to ask you a few questions.")
print ("do you like me, %s?"% user_name)
likes= input(prompt)

print ("where do you live, %s?"% user_name)
lives= input(prompt)

print ("what kind of computer do you have?")
computer=input(prompt)

print ("""
alright, so you said %r about likeing me.
you live in %r. not sure where that is.
and you have a %r computer. nice.
""" %(likes, lives,computer))