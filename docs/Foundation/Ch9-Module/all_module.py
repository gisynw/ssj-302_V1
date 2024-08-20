'test __all__ parameter in module'

def hello():
    print("Hello, Python")
def world():
    print("Python World is funny")
def test():
    print('--test--')


# Define __all__ parameter, default only import hello and world two unit
__all__ = ['hello','world']