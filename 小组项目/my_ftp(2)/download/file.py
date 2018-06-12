import os
import time


class File(object):
    def __init__(self, filename='', filesize=0, server_path='', file_last_mtime='', file_create_time=''):
        self.filename = filename
        self.filesize = filesize
        self.server_path = server_path
        self.file_last_mtime = file_last_mtime
        self.file_create_time = file_create_time

    def create_file(self, file_path):
        self.filename = os.path.split(file_path)[-1]
        self.filesize = os.path.getsize(file_path)
        self.filelocal_path = os.path.split(file_path)[0]
        self.filetype = None
        self.usrid = None

    def get_info(self):
        return (self.filename, self.filesize, self.server_path, self.file_last_mtime, self.file_create_time)

    def get_info_for_pack(self):
        return (self.filename, str(self.filesize), self.server_path, self.file_last_mtime, self.file_create_time)

    def get_name(self):
        return self.filename

    def get_size(self):
        return self.filesize

    def get_local_path(sel¯•
def main():
    import time
    f = File()
    f.create_file('/Users/liwenhui/Desktop/my_ftp/file.py')
    f.set_last_mtime('2108-01-01 07:22:22')
    f.set_file_create_time('2108-01-01 07:22:22')
    f.set_server_path('')
    print(f.pack())
    f1 = File()
    f1.unpack(f.pack())
    print(f1.pack())


if __name__ == '__main__':
    main()
