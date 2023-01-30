#object counter using oops
class Test:
    counter=0
    def __init__(self):
        Test.counter=Test.counter+1 
    @classmethod
    def m1(cls):
        print(cls.counter)   
Test()
Test()
Test()
Test.m1()
