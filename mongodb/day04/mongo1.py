#索引和聚合操作演示
from pymongo import MongoClient,IndexModel

conn = MongoClient('localhost',27017)
db = conn.stu
my_set = db.class5

#创建索引
# index = my_set.ensure_index('name')
#返回索引名称
# print(index)
#复合索引
# index = my_set.ensure_index([('name',1),('king',-1)])
# cls = db.class1
#唯一索引
# index = cls.ensure_index('name',unique=True)
#稀疏索引
# index = my_set.ensure_index('king_name',sparse = True)
# print(type(index))

#删除索引
#参数为索引名称
# my_set.drop_index('name_1')
# 删除全部索引
# my_set.drop_indexes()

#同时创建多个索引
# index1 = IndexModel([('name',1),('king',-1)])
# index2 = IndexModel([('king_name',1)])
# indexes = my_set.create_indexes([index1,index2])

#查看索引
# for i in my_set.list_indexes():
# 	print(type(i))

#聚合管道
# l = [{'$group':{'_id':'$king','count':{'$sum':1}}},{'$match':{'count':{'$gt':1}}}]
# for i in my_set.aggregate(l):
# 	print(i)