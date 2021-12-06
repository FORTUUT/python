'''
ANSI文件转UTF-8
'''
import codecs
import os


def utf_ansi(ar):  # 文件所在目录
    file_path = r'{0}'.format(ar)
    files = os.listdir(file_path)

    for file in files:
        file_name = file_path + '\\' + file
        f = codecs.open(file_name, 'r', 'ansi')
        ff = f.read()
        file_object = codecs.open(file_path + '\\' + file, 'w', 'utf-8')
        file_object.write(ff)
    return 'ok'


ar = input("文件夹地址:")
utf_ansi(ar=ar)
print('ok')
