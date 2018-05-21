 # 2.有两个列表：
 #        no = [1001,1002,1003,1004]
 #        names = ['Tom','Jerry','Spike','Tyke']
 #        用no中的编码作为键，以names中的字符串作为值，生成相应的字典

def my_zip(l1,l2):
    return {l1[n]:l2[n]  for n in range(len(l1))}

no = [1001,1002,1003,1004]
names = ['Tom','Jerry','Spike','Tyke']
print(my_zip(no,names))

