#用来获取数据库中gridfs存储文件
from pymongo import MongoClient
#和pymongo绑定的
import gridfs

conn = MongoClient('localhost',27017)
db = conn.get_database('grid')
#获取gridfs对象
fs = gridfs.GridFS(db)

files = fs.find()
for file in files:
	if file.filename =='./生日快乐歌.mp3':
		with open(file.filename,'wb') as f:
			while True:
				#file.read()函数可以获取文件内容
				data = file.read(64)
				if not data:
					break
				f.write(data)
conn.close()

		
