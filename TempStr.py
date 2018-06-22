import os
tempstr=input("请输入带有符号的温度值：")
if tempstr[-1] in ['F','f']:
    c=(eval(tempstr[:-1]-32))/1.8
    print("转换后温度为：{:.2f}C".format(c))
elif tempstr[-1] in ['c','C']:
    f=1.8*eval(tempstr[:-1])+32
    print("转换后温度为：{:.2f}F".format(f))
else:
    print("输入格式有误")
os.system("pause")