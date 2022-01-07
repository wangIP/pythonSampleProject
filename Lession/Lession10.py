#函式預設值
def say(msg='hello1'):
    print(msg)
say('hello')
say()

def say2(*msg):
    print(sum(msg))
say2(int('1'),int('2'))