print('#算法1')
a = [100]
def test(x):
    x = x + x
    print(x)
test(a)
print(a)

print('#算法2')
a = [100]
def test(x):
    x += x
    print(x)
test(a)
print(a)