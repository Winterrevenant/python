s = "Hello World"
def lenght(s):
    return len(s.strip().split()[-1])

x=lenght(s)

print(x)