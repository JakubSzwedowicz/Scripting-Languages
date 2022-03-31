args = [1, 2, 3]
kwargs = {1:'One', 2:'Two', 3:'Thress'}

def run():
    # task_1()
    # task_2()
    task_3()


def task_1():
    foo(1, 2, 3, first="one", mid='two', last='three')


def task_2():
    def foo2():
        fun = foo
        global args
        args.append(4)
        fun(args, kwargs)

    args = [1, 2]
    foo2()


def task_3():
    source = CreateFunction('-')
    exec(source)

def CreateFunction(operator: str):
    return'''
print('Ugly function')
print('Formula with operator 3 {0} 5 equals = ', (3{0}5))
'''.format(operator)


def ugly(a: int, b: int) -> None:
    print('{0} and {1} passed'.format(a, b))
    print('Sum equals = ', (a+b))


def foo(*args,**kwargs) -> None:
    [print(x) for x in args]

    for k, v in kwargs.items():
        print('Key "{0}" = value "{1}"'.format(k, v))

