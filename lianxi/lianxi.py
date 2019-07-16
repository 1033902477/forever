import logging

def fun(func):
    def user_zhuangshi(*args, **kwargs):
        aa = func(*args, **kwargs)
        print(aa)
        return aa
    return user_zhuangshi




class e:

    def __init__(self, c):
        self.c = c

    @fun
    def bar(self):
        a = self.c
        return a


if __name__ == '__main__':
    e(c=3).bar()