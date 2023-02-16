input1 = "teste"
input2 = "teae"
d = {}

def f(a, b):
    s = ""
    for i in a:
        d[i] = 0
    for i in b:
        if i in d:
            d[i] += 1
    for i in sorted(d):
        if d[i] > 0:
            s += i +str(d[i])
    return s

print(f(input1, input2))