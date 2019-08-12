
import re
import os
import requests
from multiprocessing import Process


def download_page(start,end):
        for i in range(start,end):
            url = 'http://op.hanhande.net/shtml/op_wz/list_2602_%d.shtml'%i
            response = requests.get(url)
            response.encoding = 'gbk'

            one_list = re.findall("src='(.*?)'",response.text)
            dd = requests.get(one_list)      
            aa = dd.content
            path = '/home/dj/picture'
            
            k = str(i)
            img_name = k + '.jpg'
            img_file_name = os.path.join(path,img_name)
            
            with open(img_file_name,'wb') as f:
                f.write(aa)
            
                                                        
 
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
        
            
        
                                     
        
