import hashlib
import os
import time
import uuid

from os import path

from datetime import date, datetime

import timestamp as timestamp


def get_md5(src):
    ''' 将图片的名称转换md5值 '''
    m = hashlib.md5(src.encode('utf-8'))
    # m.update(src)
    return m.hexdigest()


def rename_files():
    path = r'E:\迅雷下载\1'
    for file in os.listdir(path):
        print(file)
        if os.path.isfile(os.path.join(path, file)) == True:
            if file.find('.') < 0:
                newname = uuid.uuid1()
                # os.rename(os.path.join(path, file), os.path.join(path, newname))
                os.rename(file, newname)
                print(file, 'ok')
                # print file.split('.')[-1]


def write_to_text():
    ''' 将图片注册信息写入到dataset.txt文件中'''
    with open(r'E:\dataset.txt', 'w') as f:
        file_dir = r'E:\迅雷下载'
        for root, dirs, files in os.walk(file_dir):
            print(dirs)
            for name in files:
                f.writelines(
                    '86.747.028/' + str(uuid.uuid1()) + '  '
                    + name + '  '
                    + "by LiJuan" + '  '
                    + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '  '
                    + str(datetime.utcnow()) + '  '
                    + os.path.join(file_dir, name) + '\n')
                # list_set = [get_md5(name),
                #             "by LiJuan",
                #             time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                #             os.path.join(os.getcwd(), name)]
                # f.writelines(list_set)
                # f.writelines('\n')


if __name__ == "__main__":
    rename_files()
    # write_to_text()
