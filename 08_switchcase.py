def one():
    return "one"

def two():
    return "two"

def three():
    return "three"

switcher = {
    1: one,
    2: two,
    3: three
}

value = 2
result = switcher.get(value, lambda: "unknown")()
print(result)