def test():
    """Stupid test function"""
    l = [i for i in range(100)]
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))



