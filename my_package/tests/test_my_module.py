# Module tests

def test_my_module(my_fixture): 
    from my_package.my_module import MyClass, MySubclass

    assert MyClass().my_attr == 'attr'
    sub = MySubclass()
    assert sub.my_attr2 == 'attr2'
    assert sub.my_method() == 1
    assert sub.my_method2() == 2

def test_my_submodule():
    from my_package.my_submodule import MyUtil

    assert MyUtil()


