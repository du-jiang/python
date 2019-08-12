import re
def password(func):
    def wqrt(*args,**kwargs):
        lowerRegex = re.compile('[a-z]')
        upperRegex = re.compile('[A-Z]')
        digitRegex = re.compile('[0-9]')
        while True:
            if lowerRegex.search(pd) == None:
                print('未包含小写字母')
            elif upperRegex.search(pd) == None:
                print('未包含大写字母')
            elif digitRegex.search(pd) == None:
                print('未包含数字')
            else:
                print('输入成功')
        return func(*args,**kwargs)
    return wqrt
    