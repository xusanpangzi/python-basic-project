import os
def dayUP(df):
    dayup=1
    for i in range (365):
        if i%7 in [6,0]:
            dayup*=(1-0.01)
        else:
            dayup*=(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:#每天都努力 一年的提高
    dayfactor+=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
os.system("pause")