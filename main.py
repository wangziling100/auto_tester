import random
import re
import string


class Tester:
    
    def __init__(self, obj, rep_fn, name=None):
        self.name = name
        # list of methods
        self.meths = [i for i in dir(obj) if callable(getattr(obj, i))]
        # information of methods, including param num, type
        self.meths_detail = {}

    def test(self, obj):
        # run through the methods
        for meth in self.meths:
            if meth is '__init__':
                continue
            n = self._detect_param_num(getattr(obj, meth))

    def method_test(self, func):
        pass

    def _gen_report(self, fn):
        pass

    def _detect_param_num(self, fn):

        try:
            fn()
            return 0
        except TypeError as e:
            n = re.search('(?<=takes exactly )[0-9]*(?= arguments)', str(e))
            return n.group(0)
        except:
            return 0

    def _gen_param(self, dtype, upper=10000, lower=-10000):
        if dtype is int:
            return random.randint(lower, upper)
        if dtype is float:
            return random.random()-0.5*2*upper
        if dtype is str:
            cands = string.letters+string.digits+string.whitespace
            length = random.randint(0, 10)
            return ''.join(random.choice(cands) for i in range(length))

    def _gen_list(self, dtype, n):
        ret = []
        for i in range(n):
            ret.append(self._gen_param(dtype))
        return ret

    def _gen_params(self, n):
        pass


class example:

    def __init__(self):
        pass

    def func1(self, l, a, b, c, d, e, f, g, h, i, j):
        m, n = l
        pass

    def func2(self, i):
        print(i)


if __name__ == '__main__':
    exam1 = example()
    tester = Tester(obj=exam1, rep_fn='.')
    tester.test(exam1)
    tester.method_test(exam1.func1)

