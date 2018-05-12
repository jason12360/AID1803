# #之前的方法
# a = 10
# try:
#     b = a / '1'
# except TypeError as e:
#     print(e)

# print("-----------")
#使用 traceback
import traceback
a = 10
try:
    b = a / '1'
except TypeError:
    # print(e)
    traceback.print_exc()

print("-----------")