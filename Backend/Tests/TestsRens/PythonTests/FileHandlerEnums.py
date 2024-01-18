class SomeClass(object):
    @classmethod
    def func1(cls, arg1):
        print("Called func1({})".format(arg1))

    @classmethod
    def func2(cls, arg1):
        print("Call func2({})".format(arg1))

    @classmethod
    def func3(cls, arg1):
        print("Don't know function ''")

# can't create function map until class has been created
SomeClass.func_map = {
    'func1': SomeClass.func1,
    'func2': SomeClass.func2
}

if __name__=='__main__':
    funcList = {'func1':True, 'func2':False}
    SomeClass.func3('Argumentus-Primus')