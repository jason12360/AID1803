 # 有字符串列表如下
 #        l = ['tarena','xiaozhang','hello']
 #        生成如下字典：
 #        d = {'terena':6,'xiaozhang':9,'hello':5}

l = ['tarena','xiaozhang','hello']
d = {x:len(x) for x in l}
print(d)