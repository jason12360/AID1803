#将文件以二进制存到数据库
from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.file
my_set = db.img
# with open('test.jpg','rb') as f:
# 	#将读取的二进制流变为bson格式二进制的字符串
# 	data = f.read()
# 	content = bson.binary.Binary(data)
# my_set.insert({'name':'test.jpg','data':content})

#提取文件
data = my_set.find_one({'name':'test.jpg'})
with open('test.jpg','wb') as f:
	f.write(data['data'])

