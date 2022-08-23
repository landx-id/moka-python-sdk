import inspect

class Test:
    a = 1


test = Test()
print(test.a)

injected_class = type(
    Test.__name__,
    Test.__bases__,
    dict(Test.__dict__),
)


for keys, value in vars(injected_class).items():
    if not keys.startswith("_"):
        setattr(Test, keys, 2)
        print('changed', keys)


print(Test.a)