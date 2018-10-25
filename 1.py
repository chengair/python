from PIL import Image
import PIL.ImageFilter,PIL.ImageDraw,PIL.ImageFont
import random
import math
import collections
import rsa
import os

key=rsa.newkeys(1028)
a=12

privatekey = key[1]#
publickey = key[0]#
#print(publickey)
#print(privatekey)

s='哈哈呵呵！！'
#bs=bytes(s,'gbk')
bs=s.encode('utf-8')
print(s)
print(bs.decode('utf-8'))
mes=rsa.encrypt(bs,publickey)
#print(mes)
mes=rsa.decrypt(mes,privatekey)
print(mes)
print(mes.decode('utf-8'))

#os.system("pause")
