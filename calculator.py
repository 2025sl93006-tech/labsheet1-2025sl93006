def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def divide(a,b):
    if b==0:
        return None
    return a/b

if __name__ == "__main__":
    assert add(2,3) == 5
    print("All tests passed")
