# 20-03-10
# EX 42.8

def html_tag(tag):
    def trace(func):
        def wrapper():
            r = '<' + tag + '>' + func() + '</' + tag + '>'     
            return r
        return wrapper
    return trace

a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())
