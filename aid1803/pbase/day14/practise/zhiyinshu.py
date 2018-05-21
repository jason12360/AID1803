# 3.分解质因数：
#         输入一个正整数，分解质因数：
#         如90 则打印：
#             90=2*3*3*5


# def get_prime(n):
#     L = []   
#     if is_prime(n):
#         L.append(n)
#         return L
#     else:
#         for i in range(2,n):
#             if is_prime(i) and n % i  == 0:
#                 L.append(i)
#                 L.extend(get_prime(n//i))
#                 return L

# def get_prime(n):
#     L = []
#     b = n
#     if is_prime(n):
#         L.append(n)
#         return L
#     else:
#         while not is_prime(b):
#             for a in range(2,b):
#                 if is_prime(a) and b% a == 0:
#                     L.append(a) 
#                     b = b//a
#                     break
#         L.append(b)
#         return L


# def is_prime(j):
#     for k in range(2,j):
#         if j % k == 0:
#             return False
#     else:
#         return True


def get_prime(n):
    b = n
    k = 2
    L = []
    while k <= b:
        if b % k == 0:
            L.append(k)
            b = b//k
            k = 2
        else: 
            k += 1
    return L



print(get_prime(1000000))


