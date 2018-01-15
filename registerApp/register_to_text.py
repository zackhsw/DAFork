import os, datetime, platform, hashlib, requests
import socket, time
from os import path
# from utils import timezone
from random import choice


class GetFileDetail():
    def get_owner(self):
        '''
        获取数据拥有者公钥
        :return:
        '''
        owner_list = ['4d c9 68 ff 0e e3 5c 20 95 72 d4 77 7b 72 15 87',
                      'd3 6f a7 b2 1b dc 56 b7 4a 3d c0 78 3e 7b 95 18',
                      'af bf a2 00 a8 28 4b f3 6e 8e 4b 55 b3 5f 42 75',
                      '93 d8 49 67 6d a0 d1 55 5d 83 60 fb 5f 07 fe a2',
                      ]
        return choice(owner_list)

    # 文件名, 文件类型
    def get_name(self, joinRN):
        print('文件名：' + path.basename(joinRN))
        filename = path.basename(joinRN)
        return filename

    # 文件位置：
    def get_root(self, joinRN):
        print('文件位于：' + joinRN)
        return joinRN

    # # 文件属性
    # fileAttr = win32file.GetFileAttributes(pname)
    # print('文件属性为：' + str(fileAttr))
    # # 测试是否为Windows系统
    # #if 'Windows' in platform.system():
    # #    import win32file,win32con
    # # 查找隐藏文件及文件夹
    # fileAttr = win32file.GetFileAttributes(join(root, name))
    # if fileAttr & win32file.FILE_ATTRIBUTE_HIDDEN:
    #     print('此文件为隐藏文件：' + str(fileAttr))
    #     print('文件名：' + name)
    # fileRootAttr = win32file.GetFileAttributes(root)
    # if fileRootAttr & win32file.FILE_ATTRIBUTE_HIDDEN:
    #     print('此文件夹为隐藏文件夹：' + str(fileRootAttr))
    #     print('文件夹名：' + root)

    # 文件大小
    def get_size(self, joinRN):
        print(path.getsize(joinRN))
        return path.getsize(joinRN)

    # 文件创建时间
    def get_cdate(self, joinRN):
        filecdate = path.getctime(joinRN)
        cdate = datetime.datetime.fromtimestamp(filecdate)
        # print('文件创建时间于：' + date.strftime('%Y-%m-%d %H:%M:%S'))
        # print('文件创建时间于：' + cdate)
        return cdate

    # 文件修改时间
    def get_mdate(self, joinRN):
        filemdate = path.getmtime(joinRN)
        mdate = datetime.datetime.fromtimestamp(filemdate)
        # print('文件修改时间于：' + mdate)
        return mdate

    # 当前时间
    def get_date(self):
        # date = datetime.datetime.now()
        date = datetime.timezone.now()
        return date

    # 对文件计算Hash值
    def get_md5(self, joinRN):
        self._md5(joinRN)
        return self._md5(joinRN)

    def _md5(self, joinRN):
        m = hashlib.md5()
        maxbuf = 8192
        # with open(joinRN, 'rb') as mfile:
        try:
            mfile = open(joinRN, 'rb')
            buf = mfile.read(maxbuf)
            mfile.close()
            m.update(buf)
            md5value = m.hexdigest()
            return md5value
        except:
            print('文件被占用，等待1秒再读取')
            time.sleep(1)
            self._md5(joinRN)

    # 文件（IP+时间）计算Hash值
    # iplist[3] = str(filecdate)  # 将文档创建时间添加到idlist 覆盖None的位置
    # print(idlist)
    # data_id = filedetail.get_data_identification(iplist)  # 将idlist传到函数进行hash处理，产生数据id
    # print(data_id)

    # 分离扩展名
    def get_ext(self, joinRN):
        filename_tup = os.path.splitext(joinRN)
        filename_ext = filename_tup[1]
        # print('文件类型为：' + filename_ext[1:])
        return filename_ext[1:]

    # 获取到本机ip地址
    def get_ip(self):
        user_ip = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
        return user_ip

    # 获取本机计算机名
    # [该方法还未测试]
    # def get_pcname(self):
    #     pc_name = socket.getfqdn(socket.gethostname())
    #     return pc_name

    # 获取本机的公网ip，是通过ip138网站爬取到的
    def get_out_ip(self):
        url = r'http://1212.ip138.com/ic.asp'
        r = requests.get(url)
        txt = r.text
        ip = txt[txt.find("[") + 1: txt.find("]")]
        # print('ip:' + ip)
        return ip

    # 对所有信息, 进行sha256哈希算法加密，获取摘要，来做数据标识
    def get_data_identification(self, joinRN):
        # id_items = args
        ide = [self.get_owner(),
               self.get_md5(joinRN),
               self.get_name(joinRN),
               self.get_root(joinRN),
               self.get_ext(joinRN),
               str(self.get_cdate(joinRN)),
               str(self.get_mdate(joinRN)),
               str(self.get_date()),
               str(self.get_size(joinRN)),
               str(self.get_ip()),
               # str(self.get_out_ip())
               ]
        id_str = "".join(ide)
        d = hashlib.sha256()
        d.update(id_str.encode())
        return d.hexdigest()
        # print(d.hexdigest())
        # for item in args:
        #     d.update(item.encode())
        #     print(d.hexdigest())

        # 存于List中（resname, ctime, url, type, size）
        # rowtup = (name, date.strftime('%Y-%m-%d %H:%M:%S'), root, filename_ext[1:], getsize(join(root, name)))
        # def get_rowtup(self, joinRN):
        #     rowtup = [self.get_name(joinRN), self.get_ext(joinRN)]
        #     return (rowtup)

def write_to_text(body):
    with open(r'E:\datset.txt', 'w') as f:
        file_dir = 'E:\\dataset'
        for root, dirs, files in os.walk(file_dir):
            for name1 in dirs:
                print('dirs:' + name1)
            for name in files:
                f.writelines(body.get_md5(name) + '\n')


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'DAFork.settings'
    # file_dir = 'E:\\dataset'
    get_file = GetFileDetail()
    write_to_text(get_file)
    # for root, dirs, files in os.walk(file_dir):
    #     for name in files:
    #         print("files:"+name)
    #         # print(get_file.get_name(dirs))
