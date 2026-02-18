"""Python module"""

import sys, os, re
from my_package.my_module import my_submodule

class MyClass():
    def __init__(self):
        self.my_attr = 'attr'

    def my_method(self):
        return 1
        
class MySubclass(MyClass):
    def __init__(self):
        self.my_attr2 = 'attr2'
        super().__init__()

    def my_method2(self):
        return 2

