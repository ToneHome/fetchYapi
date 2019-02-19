#coding:utf-8

import os
import zipfile
import shutil
def mkdir(path,content=""):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        createFile(path,content)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        shutil.rmtree(path)
        createFile(path)
    return True

def createFile(path,content=''):
    if path.find('.') >= 0:
        f = open(path, 'w',encoding='utf8')
        f.write(content)
        f.close()
    else:
        os.makedirs(path)
    print
    path + ' 创建成功'

def dfs_get_zip_file(input_path,result):

#
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'/'+file):
            dfs_get_zip_file(input_path+'/'+file,result)
        else:
            result.append(input_path+'/'+file)

def zip_path(input_path,output_path,output_name):

    f = zipfile.ZipFile(output_path+'/'+output_name,'w',zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path,filelists)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path+r"/"+output_name


def shpFilesToZips(filepath):
	shpname = os.path.basename(filepath)
	shppath = os.path.dirname(filepath)

	name = shpname.replace(".shp","")
	zippath = os.path.join(shppath, name + ".zip")
	# Get the files will be packaged
	files =[]
	# package
	pre_len = len(os.path.dirname(shppath))
	zipf = zipfile.ZipFile(zippath, 'w')
	for parent, dirnames, filenames in os.walk(shppath):
		for filename in filenames:
			if '.zip' in filename:
				continue
			if name in filename:
				pathfile = os.path.join(parent, filename)
				arcname = pathfile.replace(shppath, '')
				zipf.write(pathfile, arcname)
				files.append(pathfile)
	zipf.close()


	# delete files
	for file in files:
		if os.path.exists(file):
			os.remove(file)

	return zippath