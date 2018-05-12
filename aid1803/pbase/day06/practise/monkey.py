# 1.有一只猴子摘了很多桃
#     第一天吃了全部桃子的一半，感觉不抱又吃了一个
#     第二天吃了剩下的一半，感觉不抱又吃了一个
#     。。。。以此类推
#     到第十天发现只剩下一个了
#     请问第一天摘了多少个桃

# tao = 1
# for i in range(9):
#     tao = (tao+1)*2
# print('第一天摘了',tao)


def peachleft(n):
    if n==10:
        return 1
    else:
        return (peachleft(n+1)+1)*2

tao = peachleft(1)
print('第一天摘了',tao)