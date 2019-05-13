import random
import re


class Tester:
    
    def __init__(self, rep_fn, name=None):
        self.name = name
        # list of methods
        self.meths = []
        # information of methods, including param num, type
        self.meths_detail = {}

    def _data_gen(self, dtype=None, length=None):
        pass

    def _gen_list(self, dtype, length):
        pass

    def test(self, obj):
        # get all methods
        meths = [i for i in dir(obj) if callable(getattr(obj, i))]

        # run through the methods
        for meth in meths:
            if meth is '__init__':
                continue
            getattr(obj, meth)(1)

    def method_test(self, func):
        pass

    def _gen_report(self, fn):
        pass


class example:

    def __init__(self):
        pass

    def func1(self, l):
        a, b = l
        print(a, b)

    def func2(self, i):
        print(i)


if __name__ == '__main__':
    tester = Tester(rep_fn='.')
    exam1 = example()
    tester.test(exam1)
    tester.method_test(exam1.func1)

