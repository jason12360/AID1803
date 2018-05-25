#演示通过pymongo进行增删改查操作
from pymongo import *

#创建连接对象
conn = MongoClient('localhost',27017)
#创建数据库和集合对象
db = conn.get_database('stu')
my_set = db.get_collection('class5')
#增加操作——————————————————————————————————————————————————————
# my_set.insert({'name':'张铁林','king':'乾隆'})
# my_set.insert([{'name':'张铁林','king':'乾隆'},
# 	           {'name':'张国立','king':'康熙'}])
# my_set.save({'name':'唐国强','king':'雍正'})
# my_set.save({'name':'陈建兵','king':'雍正'})

#删除操作————————————————————————————————————————————————————————————
# my_set.remove({'name':'吴奇隆'},multi=False)

#查找操作——————————————————————————————————————————————————————————
# cursor = my_set.find({},{'_id':0})
# for c in cursor:
# 	print(c)
# db = conn.get_database('stu')
# my_set = db.get_collection('class1')
# cursor = my_set.find({'gender':{'$exists':True}},{'_id':0})
# for i in cursor.sort([('name',1)]):
# 	print(i)
#示例find_one——————————————————————————————————————————————————
# dic = {'$or':[{'name':{'$gt':'Tom'}},{'gender':'w'}]}
# data = my_set.find_one(dic)

#修改操作——————————————————————————————————————————————————————
# my_set.update({'name':'张国立'},{'$set':{'name':'国立'}})
#如果文档不存在，插入文档————————————————————————————————————————————
# my_set.update({'name':'冰冰'},{'$set':{'king':'武则天'}},upsert = True)
#同时修改多条文档——————————————————————————————————————————————————————
# my_set.update({'king':'康熙'},{'$set':{'king_name':'玄烨'}},multi=True)
#使用update_many————————————————————————————————————————————————————————
# my_set.update_many({'king':'雍正'},{'$set':{'king_name':'胤禛'}})
#使用update_one——————————————————————————————————————————————————————————
# my_set.update_one({'king_name':None},{'$set':{'king_name':'弘历'}})

#使用长函数find_one_and_delete(),查找并删除，查找结果返回————————————————————
# print(my_set.find_one_and_delete({'name':'冰冰'}))


conn.close()


