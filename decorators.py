
def printer(fun):
    def new_fun(*args, **kwargs):
        print(*args, **kwargs)
        return fun(*args, **kwargs)
    return new_fun




@printer
def add(x, y):
    return x + y

@printer
def sub(x, y):
    return x - y

add(2, 3)
add(2, 3)
add(2, 3)
sub(55, 3)