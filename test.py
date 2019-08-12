import time
def count(func):
    def wqrt(*args,**kwargs):
        num = kwargs['num']
        if num > 4:
            print('404,请五秒后访问')
            time.sleep(5)
            
        else:
            return func(*args,**kwargs)
    return wqrt
