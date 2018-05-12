def get_age():
    a = int(input('请输入年龄：'))
    assert a < 140,'年龄不可能大于140！'
    assert a >= 0, '年龄不可能出现负数！'
    return a

try:
    age = get_age()
    
except AssertionError as e:
    print(e)
    age = 0
print(age)