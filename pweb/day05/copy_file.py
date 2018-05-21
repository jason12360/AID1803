import multiprocessing as mp
import os


def copydata(source_file, dest_file, start, end, buffer_size=1024):
    with open(source_file, 'rb') as file_read:
        with open(dest_file, 'wb') as file_write:
            file_read.seek(start)
            read_times = (end - start) // buffer_size
            for i in range(read_times):
                data = file_read.read(buffer_size)
                file_write.write(data)
            data = file_read.read((end - start) % buffer_size)
            file_write.write(data)


def main():
    SOURCE_FILE = 'test.jpg'
    DEST_FILE1 = 'test_dest1.jpg'
    DEST_FILE2 = 'test_dest2.jpg'
    BUFFER_SIZE = 1024
    file_size = os.path.getsize(SOURCE_FILE)
    file_mid_point = int(file_size/2)
    p1 = mp.Process(target=copydata, args=(
        SOURCE_FILE, DEST_FILE1, 0, file_mid_point, BUFFER_SIZE))
    p2 = mp.Process(target=copydata, args=(
        SOURCE_FILE, DEST_FILE2, file_mid_point, file_size, BUFFER_SIZE))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()

# def copy_first_half(source_file,dest_file):
#     size = os.path.getsize(source_file)
# 	n = int(size/2)
# 	# with open(source_file,'rb') as file_read:
# 	# 	with open(dest_file,'wb') as file_write:
# 	# 		size_read = 0
# 	# 		while size_read + BUFFER_SIZE < n:
# 	# 			data = file_read.read(BUFFER_SIZE)
# 	# 			size_read += BUFFER_SIZE
# 	# 			file_write.write(data)
# 	# 		#处理剩余的字节
# 	# 		data = file_read.read(n%BUFFER_SIZE)
# 	# 		file_write.write(data)

# def copy_second_half(source_file,dest_file):
# 	size = os.path.getsize(source_file)
# 	# n = int(size/2)
# 	# with open(source_file,'rb') as file_read:
# 	# 	with open(dest_file,'wb') as file_write:
# 	# 		start = n + 1
# 	# 		file_read.seek(start)
# 	# 		data = b'123'
# 	# 		while data:
# 	# 			data = file_read.read(BUFFER_SIZE)
# 	# 			file_write.write(data)
