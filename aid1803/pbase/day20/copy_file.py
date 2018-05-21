# 实现文件的复制（建议使用二进制方式进行操作）
#     #python3 mycp.py
#     请输入源文件：
#     /etc/passwd
#     请输入目标文件：
#     ./mypass.txt
#     提示：文件复制成功或文件复制失败

def copy_file(src,des):
	try:
		with open(src,'r+b') as src_file,open(des,'w+b') as des_file:
				#如果文件太大，则分次进行搬移
			while True:
				b = src_file.read(4096)
				if not b:
					break
				des_file.write(b)
			print('文件复制成功')
	except Exception as e:
		print('文件复制失败',e)

def main():
	src = input('请输入源文件：')
	des = input('请输入目标文件：')
	copy_file(src,des)

main()