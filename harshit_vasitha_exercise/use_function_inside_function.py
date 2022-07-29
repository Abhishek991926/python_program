# program to find greter of three numbers :


def greter_two(a,b):
    if a>b:
        return a
    else:
        return b


def gretest_three(a,b,c):
    bigger=greter_two(a,b)
    return greter_two(bigger,c)

print(gretest_three(10,200,30))