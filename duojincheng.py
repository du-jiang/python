import requests
from multiprocessing import Process
# process 1: 1-15
# process 2: 15-27

"""
下载图片的时候,response.text ==> response.content
with open( mode='wb') == > open(mode='wb')
将所有的图片下载到本地一个文件夹内.
"""

def download_page(start,end):
    for i in range(start,end):
        url = 'http://op.hanhande.net/shtml/op_wz/list_2602_%d.shtml'%i
        response = requests.get(url)
        response.encoding = 'gbk'
        # HTML = response.text
        print(response.status_code)


def main():
    p1 = Process(target=download_page,args=(1,15))
    p2 = Process(target=download_page,args=(15,28))
    print('%s will be start...'%p1.name)
    print('%s will be start...'%p2.name)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('%s;%s Over!'%(p1.name,p2.name))

if __name__ == "__main__":
    main()

