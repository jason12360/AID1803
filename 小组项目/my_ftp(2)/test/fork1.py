import os
t=2
pid=os.fork()
if pid<0:
    print('error')
elif pid==0:
    print('zi:',t)
else:
    print('fu:',t)