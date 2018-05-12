import random
import string
# L = [chr(x) for x in range(ord('z')+1) if (ord('a')<=x<=ord('z') or ord('A')<=x<=ord('Z') or ord('0')<=x<=ord('9') or x == ord(' ') or x==ord('_'))]
#生成包含A-Z，a-z，0-9，空格和下划线的字符串
L = string.ascii_letters + string.digits+'_ '
s =''.join(map(lambda c:random.choice(L),range(6)))
print(s)
