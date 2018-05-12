class Mylist(list):
    def insert_head(self,element):
        self[0:0] = [element]

L = Mylist(range(5))
L.insert_head(-1)
print(L)
