import time


"""Decorator to track function execution time"""
def benchmark(f):
    def func(*args, **keyArgs):
        t1 = time.time()
        r = f(*args, **keyArgs)
        t2 = time.time()
        t = ( t2-t1 )*1000
        print(f'Func: {f.__name__}, Time={t}miliseconds')
        return r
    
    return func