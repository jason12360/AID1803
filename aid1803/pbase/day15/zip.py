numbers = [10086,10000,10010,95588]
name = ['中国移动','中国电信','中国联通']
for t in zip(numbers,name):
    print(t)
print(dict(zip(numbers,name)))