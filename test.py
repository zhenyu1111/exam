from PIL import Image
import numpy as np
from skimage import io
import os
import sys
err1_v1=[]
err1_v2=[]
err1_v3=[]
err2_v1=[]
err2_v2=[]
err2_v3=[]
filename = 'error.txt'
file = open("error.txt", 'w')
big_path=r'D:\new1\new'
dir = os.listdir(big_path)# 获取多个文件夹的路径的列表名称，并返回一个可迭代对象
for file1 in dir:# 将可迭代对象进行循环获取，赋值给file1
    file1_path = os.path.join(big_path,file1 )
    file2_list = os.listdir(file1_path)
    for file2 in file2_list:
        file2_path=os.path.join(file1_path, file2)#许多个病人
        file3_list=os.listdir(file2_path)
        for file3 in file3_list:#2 3
            file3_path=os.path.join(file2_path, file3)
            files_list=os.listdir(file3_path)
            for files in files_list:#1069
                files_path=os.path.join(file3_path, files)
                if files_path.endswith(".tif"):
                    image = io.imread(files_path)
                    n=image.shape
                    '''print(files_path)
                    print(files_path[59:67])'''

                    if n[0] == 6:
                        err1_v1 = np.mean(abs(image[0] - image[2]))
                        err2_v1 = np.mean(abs(image[0] - image[4]))
                        err1_v2 = np.mean(abs(image[1] - image[3]))
                        err2_v2 = np.mean(abs(image[1] - image[5]))

                    if n[0] == 9:
                        err1_v1 = np.mean(abs(image[0] - image[3]))
                        err2_v1 = np.mean(abs(image[0] - image[6]))
                        err1_v2 = np.mean(abs(image[1] - image[5]))
                        err2_v2 = np.mean(abs(image[1] - image[7]))
                        err1_v3 = np.mean(abs(image[2] - image[6]))
                        err2_v3 = np.mean(abs(image[2] - image[8]))
                    print(err1_v1)
                    err1 = err1_v1 + err1_v2 + err1_v3
                    err2 = err2_v1 + err2_v2 + err2_v3
                    print(err1)
                    if err1 < err2:
                        errorpath2 = os.path.join(r'D:\new1\new', file1, file2, file3, files)
                        print(errorpath2)
                        ratio2 = (err1 / err2)
                        '''judgment2 = errorpath2.split('/')[-1]'''
                        with open(filename, 'a') as f:
                            f.write(str(errorpath2) + ',' + str(ratio2) + '\n')
                            f.close()


'''judgment1 = errorpath1.split('/')[-1]'''