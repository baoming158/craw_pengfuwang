import os
from urllib import request
from craw_pengfuwang.util import file
import time



def saveImgFile(url):
    folder_name = "img/"+time.strftime("%Y%m%d", time.localtime())
    file.mkdir(folder_name)
    filename = os.path.basename(url)
    request.urlretrieve(url, folder_name + '/' + filename)
    return folder_name+"/"+filename

if __name__ == '__main__':
    img_url = "https://pic.qiushibaike.com/system/pictures/11981/119815012/medium/app119815012.jpg"
    saveImgFile(img_url)